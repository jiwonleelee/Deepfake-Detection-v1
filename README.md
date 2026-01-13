# Deepfake-Detection-Project
🛡️ Project: Deepfake Detection (Hecto Contest)
이화여자대학교 패턴인식 팀 프로젝트 (Team 5) - 내부 협업용 가이드

📅 Project Overview
대회명: 헥토(Hecto) 경진대회

목표: 오픈 데이터셋 기반 고성능 딥페이크 탐지 모델 개발

최종 제출일: 2026. 02. 02

📂 Repository Structure
본 프로젝트는 데이터 전처리부터 모델링까지의 파이프라인 흐름을 중심으로 관리합니다.

notebooks/: 단계별 실험용 코랩(.ipynb) 파일 모음

01_preprocessing/: 프레임 추출, 얼굴 영역 크롭 및 정렬(Alignment) 코드

02_modeling_exp/: 다양한 아키텍처 비교를 통한 최적의 백본(Backbone) 선정 실험

03_augmentation_exp/: 주파수 변환, 윤곽선 블러 등 고도화된 증강 기법 검증

dataset/: 사용 데이터셋(FF++, Celeb-DF)의 상세 정보 및 출처 설명 마크다운

reports/: 중간 보고서, 최종 보고서 및 발표 자료(PDF, PPT)

src/: 전처리 및 모델 학습 시 공통으로 사용되는 유틸리티 파이썬 스크립트

.gitignore: 대용량 데이터셋 및 불필요한 캐시 파일 업로드 방지

🛠️ Tech Stack & Pipeline
1. Data Strategy
FaceForensics++ (FF++) & Celeb-DF: 벤치마크 데이터셋을 결합하여 모델의 일반화 성능 확보

Management: 대용량 데이터셋은 외부 저장소(Google Drive)에 보관하며, 본 레포지토리의 dataset/ 폴더 내 문서로 구성을 관리함

2. Processing Pipeline
Preprocessing: MTCNN/RetinaFace 등을 활용한 얼굴 크롭 및 정렬을 통해 데이터 노이즈 최소화

Model Selection: SOTA 모델(Xception, EfficientNet, ViT 등) 실험 후 가장 적합한 모델 채택

Advanced Augmentation:

주파수 변환: 딥페이크 생성 시 발생하는 미세한 주파수 아티팩트 탐지

윤곽선 블러 처리: 얼굴 합성 경계면의 부자연스러운 특징 학습 극대화

Final Optimization: 하이퍼파라미터 튜닝을 통해 최종 성능 고도화

📝 To-Do List (Short-term)
[ ] dataset/ 폴더 내 FF++, Celeb-DF 스펙 정리 문서 작성

[ ] 영상 데이터 프레임 추출 및 얼굴 정렬 자동화 코드 완성

[ ] 1차 베이스라인 모델 성능 지표 기록 및 팀 내 공유

⚠️ Internal Rules
Security: 대회 종료 전까지 레포지토리는 반드시 Private 상태 유지

Version Control: 코드 수정 시 사본 파일을 만들지 말고 Commit 기능을 활용할 것

Documentation: 실험 결과 및 특이사항은 reports/ 폴더에 즉시 업데이트하여 정보 공유
