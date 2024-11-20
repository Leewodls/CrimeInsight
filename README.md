# CrimeInsight: 범죄 데이터 시각화
 울특별시 범죄 발생 및 검거 데이터를 활용하여 지역별 5대 범죄 통계를 제공하고, 이를 시각화하여 효과적으로 이해할 수 있도록 설계된 웹 기반 애플리케이션

 ## 프로젝트 목표
- 지역별 5대 범죄 발생 현황 및 검거 통계를 시각적으로 제공.
- 위험도가 높은 지역을 파악하여 안전성을 개선.
- 사용자가 안전 지도를 통해 서울시 내 CCTV 위치 및 범죄 정보를 쉽게 탐색 가능.

## 기능
#### 사용자 기능
 - 메인 페이지: 서울 지역의 안전 지도와 범죄 현황을 한눈에 확인.
 - 로그인/회원가입: 사용자 계정 생성 및 관리.
 - 안전 지도(Safe Map): Kakao Map API를 활용한 지역별 범죄 현황 및 CCTV 위치 표시.
 - 범죄 통계 시각화: 그래프 및 표를 통해 지역별 5대 범죄의 발생 및 검거 통계 제공.
#### 관리자 기능
- 데이터 추가/ 삭제/수정 : 범죄 발생및 검거 데이터 관리, CCTV 위치 데이터 관리
- 회원 관리 : 사용자 계정 정보 확인 및 권한 부여

## 시스템 구성 
<img width="324" alt="스크린샷 2024-11-20 오후 9 26 09" src="https://github.com/user-attachments/assets/5d193ba8-62d4-44fd-8733-64ea381b83b9">

- Front-End
  -Bootstrap 기반 UI 설계

- Back-End
  -Django 프레임워크 사용 데이터 처리 및 API 구현
  -카카오맵 API 사용 지도 시각화
  -MySQL 데이터베이스 연동
  
## 라이브러리
- Python: Django 기반 백엔드 로직.
- JavaScript: Kakao Map API 연동 및 동적 지도 표시.
- MySQL: 데이터 저장 및 관계형 데이터베이스 설계.
- Bootstrap: 반응형 UI 구현.
- FusionCharts: 데이터 시각화 그래프 생성.

## 화면 구성
<img width="1115" alt="스크린샷 2024-11-20 오후 9 30 20" src="https://github.com/user-attachments/assets/e4b62fb1-1328-4400-a812-51047801be8c">
<img width="1123" alt="스크린샷 2024-11-20 오후 9 30 43" src="https://github.com/user-attachments/assets/3ec73a53-fa10-4fbe-af2b-01a618395013">


## 데이터
<img width="366" alt="스크린샷 2024-11-20 오후 9 29 12" src="https://github.com/user-attachments/assets/46743b2e-c647-4077-96c4-66c9dd7eb76f">
