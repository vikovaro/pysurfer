#!/usr/bin/env python
"""
Простой тестовый скрипт PySurfer
"""

import os
from surfer import Brain
import numpy as np

print("PySurfer тестовый скрипт запущен...")

# Укажите путь к вашим данным FreeSurfer
# Замените на ваш фактический путь
subjects_dir = os.environ.get('SUBJECTS_DIR', '/usr/local/freesurfer/subjects')
subject_id = "fsaverage"  # Используем стандартный тестовый subject
hemi = "lh"
surf = "inflated"

print(f"Subjects dir: {subjects_dir}")
print(f"Subject: {subject_id}")

try:
    # Создаем мозг
    brain = Brain(subject_id, hemi, surf, 
                  subjects_dir=subjects_dir,
                  background="white")
    
    # Добавляем простую аннотацию (если есть)
    try:
        brain.add_annotation("aparc")
    except:
        print("Аннотация aparc не найдена, продолжаем без нее")
    
    # Создаем случайные данные для отображения
    # Получаем координаты вертексов
    coords, faces = brain.geo[hemi].coords, brain.geo[hemi].faces
    
    # Создаем фиктивные данные
    n_vertices = len(coords)
    data = np.random.randn(n_vertices)
    
    # Отображаем данные
    brain.add_data(data, hemi=hemi, 
                   min=0, max=1,
                   colormap="hot", 
                   colorbar=True)
    
    print("Успешно! Если вы видите окно с визуализацией мозга, PySurfer работает корректно.")
    print("Закройте окно для завершения.")
    
    # Показать мозг
    brain.show()
    
except Exception as e:
    print(f"Ошибка: {e}")
    print("\nУстранение неполадок:")
    print("1. Проверьте, что FreeSurfer инициализирован")
    print("2. Проверьте, что subject 'fsaverage' существует в SUBJECTS_DIR")
    print("3. Попробуйте установить более старую версию VTK: pip install vtk==9.1.0")