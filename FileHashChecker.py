import hashlib  # 해쉬값 계산을 위한 라이브러리 import
import argparse # 인자 처리용 라이브러리
import sys  # 
import os   # 디렉토리 읽어오기용 라이브러리
from collections import defaultdict


# argparse 설정
parser = argparse.ArgumentParser(description="해시값 취득 프로그램")

# 기본 인자들
parser.add_argument("file_path", nargs="?", help="해시값 취득할 파일 경로")  # --list만 사용할 때를 위해 text도 optional로 처리
parser.add_argument("-c", "--check", help="지정 파일과 입력한 해시값을 비교", default=None)
parser.add_argument("-a", "--algorithm", help="선택적 해시 알고리즘 (예: sha256)", default=None)
parser.add_argument("-o", "--output", help="결과를 저장할 파일 경로(.TXT, .CSV, .JSON, .MD 등(아직 txt 이외 미지원))", default=None)
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
    result = {}
    try:
        if not os.path.isfile(file_path):   # 디렉토리를 입력받았을 경우
            file_list = os.listdir(file_path)
            for file in file_list:
                full_path = os.path.join(file_path, file)
                if os.path.isfile(full_path):
                    result_hash = hashlib.new(algo) # algo 알고리즘 개체 생성
                    with open(full_path, "rb") as f:    # file_path를 읽기 전용으로 오픈
                        for chunk in iter(lambda: f.read(4096), b""):
                            result_hash.update(chunk)  # 4096b 만큼 읽어온 chunk로 업데이트
                    result[file] = result_hash.hexdigest()
                    # return result_hash.hexdigest()
        else:
            result_hash = hashlib.new(algo) # algo 알고리즘 개체 생성
            with open(file_path, "rb") as f:    # file_path를 읽기 전용으로 오픈
                for chunk in iter(lambda: f.read(4096), b""):
                    result_hash.update(chunk)  # 4096b 만큼 읽어온 chunk로 업데이트
            result[os.path.basename(file_path)] = result_hash.hexdigest()

        return result
    except ValueError:
        print(f"[오류] 지원되지 않는 알고리즘: {algo}")
        print("다음 중에서 선택하세요:")
        print(", ".join(default_algorithms))
        sys.exit(1)
    except Exception as e:
        print(f"Error : {e}")
        
    return None
    
    
# 결과 저장용
final_results = []

# 알고리즘 리스트
algorithms = [args.algorithm] if args.algorithm else default_algorithms # args.algorithm 입력받지 않은 경우, default_algorithms를 저장

# 해시값 계산 및 결과 저장
all_hashes = {}
for algo in algorithms:
    hash_result = calculate_hashes(args.file_path, algo)    # hash_result에 해시값 계산 결과를 저장(딕셔너리)
    if hash_result:
        all_hashes[algo] = hash_result
        
# [출력 형식 변경]
# 파일 기준으로 재구성
file_based_result = defaultdict(dict)  # {파일명: {알고리즘: 해시값}}

for algo, hash_dict in all_hashes.items():
    for fname, hval in hash_dict.items():
        file_based_result[fname][algo] = hval
        
final_results = []
for fname in sorted(file_based_result):
    final_results.append(fname)
    for algo in sorted(file_based_result[fname]):
        final_results.append(f"{algo} : {file_based_result[fname][algo]}")
    final_results.append("")  # 줄 바꿈

if args.check:
    found_match = False
    for fname, algos in file_based_result.items():
        for algo, hval in algos.items():
            if hval.lower() == args.check.lower():
                print(f"[일치] {algo} 해시값이 '{fname}'과 일치합니다.")
                found_match = True
    if not found_match:
        print("[불일치] 일치하는 해시값이 없습니다.")
    sys.exit(0)
    

#콘솔 출력
if final_results:
    for line in final_results:
        print(line)
else:
    print('[오류] 해시값 취득에 실패했습니다.')

# 결과를 파일로 출력(-o, --output)
if args.output:
    try:
        with open(args.output, "w", encoding='utf-8') as f:
            f.write('\n'.join(final_results))
        print(f"\n 결과가 파일에 저장됨: {args.output}")
    except Exception as e:
        print(f"[오류] 파일 저장 실패: {e}")