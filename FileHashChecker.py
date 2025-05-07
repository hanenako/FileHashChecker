# import hashlib

# def calculate_hashes(file_path):
#     md5_hash = hashlib.md5()
#     sha256_hash = hashlib.sha256()

#     try:
#         with open(file_path, "rb") as f:
#             for chunk in iter(lambda: f.read(4096), b""):
#                 md5_hash.update(chunk)
#                 sha256_hash.update(chunk)
#     except FileNotFoundError:
#         print("파일을 찾을 수 없습니다.")
#         return
#     except Exception as e:
#         print(f"오류 발생: {e}")
#         return

#     print(f"파일: {file_path}")
#     print(f"MD5    : {md5_hash.hexdigest()}")
#     print(f"SHA256 : {sha256_hash.hexdigest()}")

# if __name__ == "__main__":
#     import sys
#     if len(sys.argv) != 2:
#         print("사용법: python hash_checker.py [파일경로]")
#     else:
#         calculate_hashes(sys.argv[1])
        
import hashlib  # 해쉬값 계산을 위한 라이브러리 import
import sys  # 인자 받아와서 사용하기 위한 라이브러리

def calculate_hashes(file_path, option ):
    md5_hash = hashlib.md5()  # md5_hash를 담을 변수
    sha256_hash = hashlib.sha256()    # sha256_hash를 담을 변수
    
    try:
        with open(file_path, "rb") as f:    # file_path를 읽기 전용으로 오픈
            for chunk in iter(lambda: f.read(4096), b""):
                md5_hash.update(chunk)  # 4096b 만큼 읽어온 chunk로 업데이트
                sha256_hash.update(chunk)   # 4096b 만큼 읽어온 chunk로 업데이트
    except FileNotFoundError:
        print("File Not Found Error")
        return
    except Exception as e:
        print(f"Error : {e}")
        return
    
    print(f"File : {file_path}")
    if option == "md5":
        print(f"MD5_HASH : {md5_hash.hexdigest()}")
    elif option == "sha256":
        print(f"SHA256_HASH : {sha256_hash.hexdigest()}")
    else:
        print("option error")
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Argv Error")
    else:
        calculate_hashes(sys.argv[1], sys.argv[2])