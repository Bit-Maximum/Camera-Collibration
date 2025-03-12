# Camera Calibration using OpenCV
_Автор: Меркурьев М. А._\
_Дальневосточный федеральный университет, 2025_

## Описание проекта

Этот проект выполняет калибровку камеры с использованием OpenCV. Основная цель — найти параметры камеры (матрицу камеры и коэффициенты дисторсии) на основе изображений шахматной доски.

## Установка

Перед началом работы убедитесь, что у вас установлены Python и необходимые библиотеки.

### Установка зависимостей:

```bash
pip install opencv-python numpy
```

## Запуск

Разместите изображения шахматной доски в директорию `images/`.

### Запустите скрипт:
```
python calibration.py
```
Во время исполнения для каждого изображения будут выведены распознанные точки.
После завершения работы программы в консоль будут выведены:
- Матрица камеры
- Коэффициенты радиальных искажений
- Вектор вращения
- Вектор смещения

## Структура проекта
```
project_root/
├── images/                 # Папка с изображениями шахматной доски
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
├── calibration.py          # Основной скрипт калибровки камеры
└── README.md               # Документация проекта
```

## Результат:

### Программа выведет в консоль
- camera_matrix — матрица камеры.
- radial_distortion — коэффициенты радиальных искажений.
- rotation_vectors — векторы вращения.
- translation_vectors — векторы трансляции.

### Пример вывода параметров в консоль:
```
Camera matrix:
[[fx  0 cx]
 [ 0 fy cy]
 [ 0  0  1]]

Radial distortion coefficients:
[ k1, k2, p1, p2, k3 ]

Rotation vectors:
[array([...]), array([...]), ...]

Translation vectors:
[array([...]), array([...]), ...]
```

## Примечания

Убедитесь, что шахматная доска хорошо освещена и запечатлена под разными углами для повышения точности калибровки.

