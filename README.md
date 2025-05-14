# FileHashChecker 개발 체크리스트

# ✅ FileHashChecker 개발 체크리스트

---

## 📦 기본 기능

- [x]  파일의 SHA-256 해시 계산
- [x]  SHA-1, MD5 등 다른 알고리즘 선택 가능
- [x]  입력 해시와의 일치 여부 확인
- [x]  CLI로 파일 경로와 해시값 인자 받기
- [x]  잘못된 파일 경로/해시값 예외 처리

---

## 📁 확장 기능: 다중 처리 & 저장

- [x]  다중 파일 해시 일괄 검사 (폴더 지정)
- [x]  서브디렉토리 포함 검사 옵션 추가
- [x]  검사 결과를 CSV로 저장
- [x]  검사 결과를 JSON으로 저장
- [x]  검사 후 콘솔 + 파일로 동시에 출력

---

## 📄 해시 목록 파일

- [?]  해시 목록 파일(txt/csv) 불러오기
- [x]  각 파일 해시 비교 결과 표시
- [?]  누락된 파일/해시값 처리

---

## 🌐 VirusTotal 연동

- [ ]  VirusTotal API 호출 기능 구현
- [ ]  해시값으로 파일 조회
- [ ]  악성 여부, 탐지 수 등 정보 출력
- [ ]  API Key 관리 (환경변수 또는 설정 파일)

---

## 🧠 보안 유틸리티 추가

- [x]  동일 해시값을 가진 다른 파일 탐지
- [ ]  해시 충돌 경고 출력
- [ ]  파일 크기, 수정시간 비교 기능

## 🛠 설정 관리

- [ ]  기본 해시 알고리즘 설정 파일로 지정 (.json 또는 .ini)
- [ ]  출력 포맷, 저장 경로 등 설정 가능

---

## 🖥 GUI 모드 (선택 사항)

- [ ]  Tkinter 또는 PyQt로 GUI 구성
- [ ]  파일 드래그 앤 드롭
- [ ]  해시 결과 GUI에 표시
- [ ]  비교 결과 강조 색상

---

---

## 🚀 배포 및 정리

- [ ]  PyInstaller로 단일 실행 파일(.exe) 생성
- [ ]  [README.md](http://readme.md/) 작성 (사용법, 예시 등 포함)
- [ ]  GitHub에 정리하여 공개


-------------------------------------------------

FileHashChecker By Python

usage: FileHashChecker.py [-h] [-a ALGORITHM] [-o OUTPUT] [--list-algorithms] [file_path]

positional arguments:
  file_path             해시값 취득할 파일 경로

options:
  -h, --help            show this help message and exit
  -a, --algorithm ALGORITHM
                        선택적 해시 알고리즘 (예: sha256)
  -o, --output OUTPUT   결과를 저장할 파일 경로
  --list-algorithms     사용 가능한 해시 알고리즘 목록 출력

  test