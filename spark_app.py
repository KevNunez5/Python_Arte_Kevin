from pyspark.sql import SparkSession

# Crear sesión de Spark
spark = SparkSession.builder.appName("AutoMPG").getOrCreate()

# Cargar dataset
df = spark.read.csv("autos.csv", header=True, inferSchema=True)

# Limpiar y procesar
df = df.dropna(subset=["mpg", "horsepower", "weight", "cylinders"])

# Agrupar por número de cilindros y sacar promedio de MPG
result = df.groupBy("cylinders").avg("mpg").orderBy("cylinders")

# Guardar resultados
result.write.mode("overwrite").json("resultados")
