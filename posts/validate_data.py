from posts.models import Post


def validate_post():
    # 1. 모든 포스트 데이터 가져오기
    posts = Post.objects.all()

    # 2. 각각의 포스트 내용을 확인
    for post in posts:
        if '&' in post.content:
            print(post.id, '번 글에 &가 있습니다')
    # 3. &가 있다면 삭제하기
            post.content = post.content.replace('&', '')
    # 4. 저장하기
            post.save()
        if post.dt_modified < post.dt_created:
            print(post.id, '번 글에 수정일이 생성일보다 과거입니다.')
            post.save()  # dt_modified를 안바꾸고 save만해도 dt_modified는 현재시간이 됨

