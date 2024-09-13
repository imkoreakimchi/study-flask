## 회원 가입 API 만들기

- /member POST
    - req: id , pw, email을 입력 받는다.
    - res: id만 반환한다.

- /login POST
    - req: id, pw를 입력 받는다.
    - res: "로그인 완료" 라는 메시지를 반환한다.

- /member GET
    - res: "회원 가입 페이지를 작성 중 입니다" 라는 메시지를 반환한다.

- /login GET
    - res: "잘못된 HTTP 메서드를 요청 하였습니다" 라는 메시지를 반환한다.