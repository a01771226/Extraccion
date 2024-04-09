import pandas as pd

print("Aplicación de extracción de datos")
df = pd.read_excel("detalle_precios_productos_fabricados_2022.xlsx")
print(df.info())


filtro1 = df[df["NOMBRE_VENDEDOR"] == "LETICIA RAMIREZ HERNANDEZ"]
print(filtro1)
filtro1.to_csv("Entregable1.csv")

filtro2 = df.iloc[2:8,: ]
print(filtro2)
filtro2.to_csv("Entregable2.csv")

filtro3 = df.iloc[:, [1,3,4,10]]
print(filtro3)
filtro3.to_csv("Entregable3.csv")

df1= pd.read_excel("detalle_precios_productos_fabricados_2022.xlsx", index_col=1)
df1

filtro4=df1.loc[["2022-11-22","'2022-12-23"], ["SUBTOTAL_PARTIDA"]]
filtro4
filtro4.to_csv("Entregable4.csv")

filtro5=df.head(8)
filtro5
filtro5.to_csv("Entregable5.csv")

filtro6=df[df["SUBTOTAL_PARTIDA"] > 77000]
filtro6
filtro6.to_csv("Entregable6.csv")

filtro7=df[(df["SUBTOTAL_PARTIDA"] > 77000) & (df["FECHA_DOC"] == "2022-05-24")]
filtro7
filtro7.to_csv("Entregable7.csv")

filtro8=df[(df["SUBTOTAL_PARTIDA"] > 77000)| (df["FECHA_DOC"] == "2022-05-24")]
filtro8
filtro8.to_csv("Entregable8.csv")

filtro9=df[~(df["SUBTOTAL_PARTIDA"] > 77000) & ~(df["FECHA_DOC"] == "2022-05-24")]
filtro9
filtro9.to_csv("Entregable9.csv")