import hashlib  # 해쉬값 계산을 위한 라이브러리 import
import argparse # 인자 처리용 라이브러리
import sys  # 

# argparse 설정
parser = argparse.ArgumentParser(description="해시값 취득 프로그램")

# 기본 인자들
parser.add_argument("file_path", nargs="?", help="해시값 취득할 파일 경로")  # --list만 사용할 때를 위해 text도 optional로 처리
parser.add_argument("-a", "--algorithm", help="선택적 해시 알고리즘 (예: sha256)", default=None)
parser.add_argument("-o", "--output", help="결과를 저장할 파일 경로", default=None)
parser.add_argument("--list-algorithms", action="store_true", help="사용 가능한 해시 알고리즘 목록 출력")

args = parser.parse_args()

# 알고리즘 리스트(--list-algorithms)
available_algorithms = sorted(hashlib.algorithms_available)
default_algorithms = ['md5', 'sha1', 'sha256', 'sha512']

if args.list_algorithms:
    print('사용 가능한 해시 알고리즘 목록:')
    for algo in available_algorithms:
        print(f'- {algo}')
    sys.exit(0)
    
if not args.file_path:
    print('[오류] 파일을 지정하세요')
    parser.print_help()
    sys.exit(1)

#해시값 취득 함수
def calculate_hashes(file_path, algo):
    try:
        result_hash = hashlib.new(algo) # algo 알고리즘 개체 생성
        with open(file_path, "rb") as f:    # file_path를 읽기 전용으로 오픈
            for chunk in iter(lambda: f.read(4096), b""):
                result_hash.update(chunk)  # 4096b 만큼 읽어온 chunk로 업데이트
        return result_hash.hexdigest()
    except ValueError:
        print(f"[오류] 지원되지 않는 알고리즘: {algo}")
        print("다음 중에서 선택하세요:")
        print(", ".join(default_algorithms))
        sys.exit(1)
    except Exception as e:
        print(f"Error : {e}")
        
    return None
    
    #print(f"File : {file_path}")
    
    
results = []

if args.algorithm:
    result = calculate_hashes(args.file_path, args.algorithm)
    if result:
        results.append(f"{args.algorithm}: {result}")
else:
    for algo in default_algorithms:
        result = calculate_hashes(args.file_path, algo)
        if result:
            results.append(f"{algo}: {result}")

#콘솔 출력
if results:
    print("\n결과:")
    for r in results:
        print(r)
else:
    print('[오류] 해시값 취득에 실패했습니다.')
    
# 결과를 파일로 출력(-o, --output)
if args.output:
    try:
        with open(args.output, "w", encoding='utf-8') as f:
            f.write('\n'.join(results))
        print(f"\n 결과가 파일에 저장됨: {args.output}")
    except Exception as e:
        print(f"[오류] 파일 저장 실패: {e}")