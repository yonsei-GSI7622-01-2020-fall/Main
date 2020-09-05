# FAQ
매주 수업 및 과제에 대해서 나온 질문에 대한 답변

## Week-01
#### 1. git commit시 다음과 같은 메시지가 뜹니다
```
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author
```
- (Solution) 이경우에는, 다음 두 명령어를 본인의 Github 계정에 맞게 순차적으로 입력해줍니다.
```
git config --global user.name "Your Name"
git config --global user.email you@example.com
```

#### 2. git bash는 어디서 설치하나요?
- [https://gitforwindows.org/](https://gitforwindows.org/) 여기서 다운로드 받으시면 되고, 설치시 기본설정값을 유지한채 계속 Next를 눌러주시면 됩니다.
