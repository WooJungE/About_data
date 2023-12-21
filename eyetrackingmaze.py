import cv2
import torch
import numpy as np

# YOLOv5 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/SM-PC/Downloads/yolov5_best.pt')

# 원의 초기 위치 설정
circle_pos_int = [250, 70]
circle_pos_int2 = [220, 110]

# 축하 메시지를 표시하는 함수
def show_congratulation_screen():
    img = cv2.imread('C:/Users/SM-PC/Downloads/mainpage.jpg')
    cv2.putText(img, 'Congratulations!', (80, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 2)
    cv2.imshow('End', img)
    cv2.waitKey(5000) # 축하 메시지를 5초 동안 표시
    cv2.destroyAllWindows()
    exit()  # 프로그램 종료

# 메인 화면을 표시하는 함수
def show_main_screen():
    img = cv2.imread('C:/Users/SM-PC/Downloads/mainpage.jpg')
    cv2.putText(img, 'Eye Tracking Maze', (70, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 2)
    cv2.putText(img, 'Press \'e\' to start Easy mode', (60, 140), cv2.FONT_HERSHEY_DUPLEX, 0.7, (80,80,80),2)
    cv2.putText(img, 'Press \'h\' to start Hard mode', (60, 180), cv2.FONT_HERSHEY_DUPLEX, 0.7, (80,80,80), 2)
    cv2.imshow('Main', img)

end_point = None  # 미로의 종료점 위치를 저장하는 전역 변수

# 원의 위치를 업데이트하는 함수
def displayPosition(direction):
    global circle_pos, end_point
    map_height, map_width = map1.shape[:2]

    new_pos = circle_pos.copy()
    check_pos = circle_pos.copy()  # 검은 픽셀을 확인할 위치

		# 방향에 따른 원의 새 위치 계산
    if direction == 'left':
        new_pos[0] -= 2
        check_pos[0] -= 1
    elif direction == 'right':
        new_pos[0] += 2
        check_pos[0] += 1
    elif direction == 'up':
        new_pos[1] += 2
        check_pos[1] += 1
    elif direction == 'down':
        new_pos[1] -= 2
        check_pos[1] -= 1

    # 새 위치가 지도 밖에 있는지 또는 검은 픽셀인지 확인
    if (check_pos[0] < 0 or check_pos[1] < 0 or
        check_pos[0] >= map_width or check_pos[1] >= map_height or
        (map1[check_pos[1], check_pos[0]] == [0, 0, 0]).all()):
        print("Cannot move")
    else:
        circle_pos = new_pos

    display_map = map1.copy()
    cv2.circle(display_map, tuple(circle_pos), 15, (0, 0, 255), -1, 8, 0)  # 원의 색을 빨간색으로 변경

		# 원이 미로의 종료점에 도달했는지 확인
    if end_point[0] <= circle_pos[0] <= end_point[1] and end_point[2] <= circle_pos[1] <= end_point[3]:
        print("Success!")
        cv2.destroyAllWindows()
        show_congratulation_screen()

    cv2.imshow("Map", display_map)

    # 디버깅 코드
    print(f"Direction: {direction}, Circle position: {circle_pos}")


# 주어진 색이 어느 방향을 나타내는지 판단하는 함수
def is_direction_color(color):
    # 방향을 나타내는 색상 정의
    color_left = np.array([253, 179, 56])
    color_right = np.array([208, 210, 71])
    color_up = np.array([254, 114, 47])
    color_down = np.array([78, 248, 63])

    # 주어진 색상과 각 방향 색상 간의 유클리디안 거리 계산
    dist_left = np.linalg.norm(color - color_left)
    dist_right = np.linalg.norm(color - color_right)
    dist_up = np.linalg.norm(color - color_up)
    dist_down = np.linalg.norm(color - color_down)

    # 가장 가까운 방향 색상에 따라 방향 결정
    min_dist = min(dist_left, dist_right, dist_up, dist_down)
    if min_dist == dist_left:
        return 'left'
    elif min_dist == dist_right:
        return 'right'
    elif min_dist == dist_up:
        return 'up'
    elif min_dist == dist_down:
        return 'down'
    else:
        return 'default'  # 정면 응시 기본 방향

show_main_screen()

# 웹캠 열기
cap = cv2.VideoCapture(0)

# 사용자가 's'를 누를 때까지 대기
while True:

    key = cv2.waitKey(1)

    if key == ord('e'): # 's'를 눌렀을 때
        cv2.destroyWindow("Main") # "Main" 창 닫기
        map1 = cv2.imread('C:/Users/SM-PC/Downloads/maze2.jpg') # 미로 이미지 로드
        map1 = cv2.resize(map1, (500,500)) # 이미지 크기 조절
        cv2.imshow("Map", map1) # 미로 이미지 표시
        circle_pos = circle_pos_int  # 원의 위치 초기화
        end_point = [240, 255, 445, 457]  # 쉬운 모드에 대한 종료점 설정
        break
    if key == ord('h'): # 's'를 눌렀을 때
        cv2.destroyWindow("Main") # "Main" 창 닫기
        map1 = cv2.imread('C:/Users/SM-PC/Downloads/maze1.jpg') # 미로 이미지 로드
        map1 = cv2.resize(map1, (500,500)) # 이미지 크기 조절
        cv2.imshow("Map", map1) # 미로 이미지 표시
        circle_pos = circle_pos_int2 # 원의 위치 초기화
        end_point = [360, 370, 435, 445]  # 어려운 모드에 대한 종료점 설정
        break

    elif key == 27:  # ESC 키 눌렸을 때
        break

# 웹캠 열기
cap = cv2.VideoCapture(0)

# 웹캠이 열려 있는 동안 반복
while True:

		# 웹캠에서 프레임 읽기
    ret, frame = cap.read()
    if not ret: # 프레임 읽기 실패 시 반복문 종료
        break

		# 프레임 크기 조절
    frame = cv2.resize(frame, (frame.shape[1] // 2, frame.shape[0] // 2))

		# 프레임을 RGB로 변환
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

		# 객체 탐지 실행
    results = model(frame_rgb)

		# 탐지 결과 출력
    results.print()

		# 탐지 결과를 프레임에 그리기
    results.render() # 상자 및 레이블로 results.imgs 업데이트
    for img in results.ims:
				# 감지된 각 객체에 대해
        for result in results.xyxy[0]:
						# 바운딩 박스 좌표 가져오기
            x, y, w, h = result[:4]
						# 바운딩 박스의 상단 가운데 픽셀의 색 가져오기
            color = frame_rgb[int(y), int(x)]
						# 색에 따라 방향 결정
            direction = is_direction_color(color)
						# 원의 위치 업데이트
            displayPosition(direction)

        cv2.imshow('YOLOv5', img[:, :, ::-1])  # OpenCV BGR 예상

    # 'q'가 눌리면 루프 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 웹캠 해제 및 모든 창 닫기
cap.release()
cv2.destroyAllWindows()
