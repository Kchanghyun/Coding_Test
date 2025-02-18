-- 코드를 입력하세요
-- 게시글 ID, 작성자 ID, 게시글 제목, 게시글 내용, 가격, 작성일, 거래상태, 조회수
-- 댓글 ID, 게실글 ID, 작성자 ID, 댓글 내용, 작성일
SELECT b.TITLE, b.BOARD_ID, r.REPLY_ID, r.WRITER_ID, r.CONTENTS, DATE_FORMAT(r.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
FROM USED_GOODS_BOARD b
JOIN USED_GOODS_REPLY r ON b.BOARD_ID = r.BOARD_ID
WHERE DATE_FORMAT(b.CREATED_DATE, '%Y-%m') = '2022-10'
ORDER BY r.CREATED_DATE ASC, b.TITLE ASC;