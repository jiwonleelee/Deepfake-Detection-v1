# Deepfake-Detection-Project
🛡️ Project: Deepfake Detection (Hecto Contest)
팀 내부 공유용 가이드 및 진행 상황 기록

📅 Project Overview
대회명: 헥토(Hecto) 경진대회

목표: 오픈 데이터셋 기반의 고성능 딥페이크 탐지 모델 개발

최종 마감일: 2026. 02. 02

📂 Repository Structure (Updated)
전체적인 파이프라인 흐름과 문서 관리 효율성을 고려한 구조입니다.

notebooks/: 코랩(.ipynb) 작업 파일 모음

01_preprocessing/: 프레임 추출, 얼굴 크롭 및 정렬 코드

02_modeling_exp/: 모델 아키텍처별 비교 및 선정 실험

03_augmentation_exp/: 주파수 변환, 윤곽선 블러 등 고급 증강 실험

dataset/: 사용 데이터셋(FF++, Celeb-DF)의 정보 및 출처 설명 문서 보관

reports/: 프로젝트 중간/최종 보고서 및 발표 자료(PDF, PPT)

src/: 전처리 및 모델 학습에 공통으로 사용되는 파이썬 유틸리티 함수

.gitignore: 대용량 데이터 및 불필요한 캐시 파일 업로드 방지

🛠️ Tech Stack & Methodology
1. Data Strategy
FaceForensics++ (FF++) & Celeb-DF: 두 벤치마크 데이터셋을 결합하여 모델의 강건성 확보

Dataset Management: 대용량 파일은 외부 저장소에 두고, dataset/ 폴더 내 마크다운 문서를 통해 데이터 구성 및 전처리 이력을 관리함

2. Pipeline Stage
Preprocessing: 고도화된 얼굴 크롭 및 정렬(Alignment)을 통해 데이터 품질 확보

Modeling Selection: 여러 SOTA 모델을 실험하여 본 프로젝트에 가장 적합한 백본(Backbone) 선정

Advanced Augmentation:

주파수 변환: 딥페이크 생성 과정의 미세한 흔적 추적

윤곽선 블러 처리: 합성 경계면의 부자연스러움을 학습하여 탐지율 향상

Final Optimization: 하이퍼파라미터 튜닝을 통해 최종 성능 극대화

📝 To-Do List (Short-term)
[ ] dataset/ 폴더에 FF++, Celeb-DF 상세 스펙 정리 문서 작성

[ ] 영상 프레임 추출 및 얼굴 영역 정렬 자동화 스크립트 완성

[ ] 베이스라인 모델 성능 지표 기록 및 공유

⚠️ Team Rules
Private 유지: 대회 종료 시까지 절대 퍼블릭으로 전환 금지

버전 관리: 코드 수정 시 사본 파일을 만들지 말고 깃허브 커밋 기능을 활용할 것
