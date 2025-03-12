import cv2
import numpy as np
import glob

CHECKERBOARD_SIZE = (6, 9)


def get_checkerboard_points():
    """
    Generate 3D world coordinates for a checkerboard pattern.

    Returns:
        np.ndarray: A 3D array of shape (1, number_of_corners, 3) representing
        the world coordinates of the checkerboard corners, with z-coordinates set to zero.
    """
    world_points = np.zeros(
        (1, CHECKERBOARD_SIZE[0] * CHECKERBOARD_SIZE[1], 3), np.float32
    )
    world_points[0, :, :2] = np.mgrid[
        0 : CHECKERBOARD_SIZE[0], 0 : CHECKERBOARD_SIZE[1]
    ].T.reshape(-1, 2)
    return world_points


if __name__ == "__main__":
    world_points = []
    image_points = []

    checkerboard_points = get_checkerboard_points()
    image = None
    gray_image = None

    images = glob.glob("images/*.jpg")
    for image_path in images:
        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        retval, corners = cv2.findChessboardCorners(
            image=gray_image,
            patternSize=CHECKERBOARD_SIZE,
            flags=cv2.CALIB_CB_ADAPTIVE_THRESH
            + cv2.CALIB_CB_FAST_CHECK
            + cv2.CALIB_CB_NORMALIZE_IMAGE,
        )

        if retval:
            world_points.append(checkerboard_points)
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
            corners_2d = cv2.cornerSubPix(
                image=gray_image,
                corners=corners,
                winSize=(11, 11),
                zeroZone=(-1, -1),
                criteria=criteria,
            )

            image_points.append(corners_2d)
            image = cv2.drawChessboardCorners(
                image, CHECKERBOARD_SIZE, corners_2d, retval
            )

        cv2.imshow("img", image)
        cv2.waitKey(0)

    cv2.destroyAllWindows()

    h, w = image.shape[:2]
    retval, camera_matrix, radial_distortion, rotation_vectors, translation_vectors = cv2.calibrateCamera(
        objectPoints=world_points,
        imagePoints=image_points,
        imageSize=(w, h),
        cameraMatrix=None,
        distCoeffs=None
    )

    print("Camera matrix: \n")
    print(camera_matrix)
    print("\nRadial distortion coefficients: \n")
    print(radial_distortion)
    print("\nRotation vectors: \n")
    print(rotation_vectors)
    print("\nTranslation vectors: \n")
    print(translation_vectors)
