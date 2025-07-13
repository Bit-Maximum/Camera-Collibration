# 🎯 Калибровка камеры с использованием OpenCV

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/Bit-Maximum/Camera-Collibration/blob/main/README.md)
[![ru](https://img.shields.io/badge/lang-ru-blue.svg)](https://github.com/Bit-Maximum/Camera-Collibration/blob/main/translation/README.ru.md)

### Меркурьев Максим Андреевич
_Дальневосточный федеральный университет, 2025_

---

## 📚 Описание проекта

Этот проект выполняет **калибровку камеры** на основе набора изображений шахматной доски с использованием библиотеки **OpenCV**.

Цель: определить **матрицу камеры** и **коэффициенты дисторсии**, необходимые для устранения искажений изображения.

---

## 🚀 Как запустить?

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Bit-Maximum/Camera-Collibration.git
cd Camera-Collibration
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Разместите изображения шахматной доски в директорию `images/`. Пример фото сделанных на смартфон Realme C21:

![Calibration GIF](./example.gif)

> _Рекомендуется, чтобы доска занимала большую часть кадра и была заснята под разными углами._

4. Запустите скрипт:
```
python calibration.py
```

> Во время исполнения для каждого изображения будут выведены распознанные точки.

## 📂 Структура проекта
```
project_root/
├── images/                 # Папка с изображениями шахматной доски
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
└── calibration.py          # Основной скрипт калибровки камеры
```

## 🧾 Результат:

### Программа выведет в консоль:
- 📐 Матрица камеры (camera_matrix)
- 🔍 Коэффициенты искажений (radial_distortion).
- 🌀 Векторы вращения (rotation_vectors)
- 📦 Векторы смещения (translation_vectors)

### 💡 Пример вывода:
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

## 📝 Cоветы

* Используйте **чёткие фотографии** с хорошим освещением.
* Убедитесь, что шахматная доска занимает **большую часть** изображений — это улучшает точность.
* Для точной калибровки желательно иметь **хотя бы пять изображений**.
