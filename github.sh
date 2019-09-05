# Git 설치
sudo apt-get install git-core

# Github 개인 정보 등록
sudo git config --global user.name "knyfree"
sudo git config --global user.email "knyfree@naver.com"
sudo git config --global color.ui "auto"

# https://github.com/knyfree/pyspark.git

sudo git clone https://github.com/knyfree/pyspark.git # 원격 저장소 복제

# 원격 저장소 등록
sudo git remote add origin https://github.com/knyfree/pyspark.git
sudo git fetch origin

sudo git add -A # 변경된 모든 파일 추가 (커밋 전 필수 실행)

sudo git commit 

sudo git commit -m "python & pyspark" # 커밋 메세지를 입력 

sudo git push # 저장소에 올리기 (계정 암호 입력)

sudo git pull # 저장소 업데이트 (내려받기)
