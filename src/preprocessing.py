
import cv2
import numpy as np
import os

def get_aligned_face(image, face_info, target_size=(256, 256)):
    """얼굴 정렬 및 정사각 크롭 (FF++ 로직 그대로)"""
    try:
        h_img, w_img = image.shape[:2]
        landmarks = getattr(face_info, 'kps', None)
        bbox = getattr(face_info, 'bbox', None)
        if bbox is None: return None

        x1, y1, x2, y2 = bbox.astype(int)
        center_x, center_y = (x1 + x2) // 2, (y1 + y2) // 2

        # 1. 정렬 시도 (눈 위치 기준)
        if landmarks is not None and len(landmarks) >= 2:
            left_eye, right_eye = landmarks[0], landmarks[1]
            dy, dx = right_eye[1] - left_eye[1], right_eye[0] - left_eye[0]
            angle = np.degrees(np.arctan2(dy, dx))
            M = cv2.getRotationMatrix2D((float(center_x), float(center_y)), angle, 1.0)
            image = cv2.warpAffine(image, M, (w_img, h_img), flags=cv2.INTER_CUBIC)

        # 2. 정사각 크롭 영역 계산
        w_box, h_box = x2 - x1, y2 - y1
        side_length = int(max(w_box, h_box) * 1.3)
        half_side = side_length // 2
        nx1, ny1 = center_x - half_side, center_y - half_side
        nx2, ny2 = center_x + half_side, center_y + half_side

        # 패딩 처리
        pad_x1, pad_y1 = max(0, -nx1), max(0, -ny1)
        pad_x2, pad_y2 = max(0, nx2 - w_img), max(0, ny2 - h_img)
        nx1, ny1, nx2, ny2 = max(0, nx1), max(0, ny1), min(w_img, nx2), min(h_img, ny2)

        face_crop = image[ny1:ny2, nx1:nx2]
        if pad_x1 > 0 or pad_y1 > 0 or pad_x2 > 0 or pad_y2 > 0:
            face_crop = cv2.copyMakeBorder(face_crop, pad_y1, pad_y2, pad_x1, pad_x2,
                                           cv2.BORDER_CONSTANT, value=[0, 0, 0])
        return cv2.resize(face_crop, target_size)
    except:
        return None

def resize_with_letterbox(image, target_size=(256, 256)):
    """얼굴 미검출 시 전체 화면 리사이즈 (코너케이스 대응)"""
    if image.size == 0: return np.zeros((target_size[1], target_size[0], 3), dtype=np.uint8)
    h, w = image.shape[:2]
    scale = min(target_size[0]/w, target_size[1]/h)
    nw, nh = int(w * scale), int(h * scale)
    img_resized = cv2.resize(image, (nw, nh))
    canvas = np.zeros((target_size[1], target_size[0], 3), dtype=np.uint8)
    dx, dy = (target_size[0]-nw)//2, (target_size[1]-nh)//2
    canvas[dy:dy+nh, dx:dx+nw] = img_resized
    return canvas
