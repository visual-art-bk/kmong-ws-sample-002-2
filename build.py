import os
import subprocess

# 빌드할 앱의 이름과 경로를 설정합니다.
app_name = "main.exe"  # 빌드 후 생성될 파일 이름
dist_path = "dist"
app_path = os.path.join(dist_path, app_name)

# PyInstaller 빌드를 수행합니다.
subprocess.run([
    "pyinstaller",
    "--noconfirm", "--onefile", "--windowed",
    "--hidden-import=google.generativeai",
    "--hidden-import=pkg_resources.py2_warn",  # 숨겨진 패키지 로드
    f"--add-data=config.json;.",               # config.json 포함
    f"--add-data=category_urls.txt;.",         # category_urls.txt 포함
    "--runtime-hook=runtime_hook.py",          # runtime_hook.py 포함
    "main.py"
])

print(f"{app_name} 빌드가 완료되었습니다.")
