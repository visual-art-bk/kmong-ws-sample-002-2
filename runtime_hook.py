import sys
import io
import os

# UTF-8 출력 설정
if sys.stdout is not None:
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8', errors='ignore')
else:
    sys.stdout = open(os.devnull, 'w', encoding='utf-8')  # 기본 출력 대체

if sys.stderr is not None:
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8', errors='ignore')
else:
    sys.stderr = open(os.devnull, 'w', encoding='utf-8')  # 기본 오류 출력 대체
