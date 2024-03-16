# ChatGPT with Slack
현재는 작동하지 않습니다 ! </br> 


제작을 할 당시 GPT API가 출시하지 않은 상태였기에 [acheong08/ChatGPT](https://github.com/acheong08/ChatGPT)의 코드를 기반으로 연결하였다.<br>
Database는 postgresql 를 사용하며 현 레포지토리에는 이에 필요한 init.sql 파일은 올리지 않았다. <br>
Database의 컬럼은 아래와 같다.
- User_id: slack user and bot 고유 ID
- Parent_id: GPT와의 대화에 필요한 고유 ID 
- Conversation_id: 기존 대화를 지속하기 위한 고유 ID, Parent ID와 함께 사용
- Conversation: 사용자나 봇의 대화 메시지
- Created_at: 메시지의 생성 시각
- Thread_ts: 스레드의 생성 시각, 스레드 생성 시각을 통해서 슬랙 스레드에 댓글을 남김


---

슬랙봇은 [workdd/ChatGPT_with_Slack](https://github.com/workdd/ChatGPT_with_Slack) 님의 코드를 기반으로 작성함을 밝힌다.<br>
이 코드를 기반으로 필요한 부분을 수정해 재구성하였으며,<br>

