# CCTV 관제 웹 사이트

라즈베리파이의 카메라 영상을 실시간으로 받아서 이를 보여주는 관제 웹 사이트를 제작하고자 한다.<br>
여러 대의 카메라를 실시간으로 보여줄 예정이며, 카메라에서 발생하는 상황을 인지하고, <br>
이를 통계내어 연간 그래프로 보여줄 예정이다.

웹 사이트는 bootstrap에서 템플릿을 사용했으며 링크는 다음과 같다.<br>
https://startbootstrap.com/themes/sb-admin-2/

용량이 너무 많기 때문에 템플릿을 제외한 html코드와 flask코드만 업로드 한다.

- run_server.py : 페이지 렌더링 코드<br>
- index.html : 상황 발생 횟수를 통계낸 DashBoard<br>
- cctv.html : cctv영상을 실시간으로 출력하는 페이지<br>
