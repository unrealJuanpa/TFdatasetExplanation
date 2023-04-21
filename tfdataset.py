import tensorflow as tf

# Supongamos que X e Y son tus arrays de entrada y salida, respectivamente
X = ... # Datos de entrada
Y = ... # Datos de salida

# Crea un objeto `tf.data.Dataset` a partir de tus arrays de entrada y salida
dataset = tf.data.Dataset.from_tensor_slices((X, Y))

# También puedes mezclar y dividir el dataset para el entrenamiento y validación, 
# por ejemplo, para mezclar y dividir 80/20 para entrenamiento y validación
total_samples = len(X)
train_size = int(0.8 * total_samples)
val_size = total_samples - train_size

# Mezcla y divide el dataset en conjuntos de entrenamiento y validación
dataset = dataset.shuffle(total_samples)
train_dataset = dataset.take(train_size)
val_dataset = dataset.skip(train_size)

# También puedes aplicar otras transformaciones en el dataset, como 
# filtrado, mapeo, agrupación y repetición
dataset = dataset.filter(...)
dataset = dataset.map(...)
dataset = dataset.batch(...)
dataset = dataset.repeat(...)

"""
dataset = tf.data.Dataset.from_generator(
    data_generator,
    output_types=(tf.float32, tf.int32),
    output_shapes=(tf.TensorShape([None, 10]), tf.TensorShape([None]))
)
"""