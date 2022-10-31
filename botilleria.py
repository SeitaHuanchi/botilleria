# botilleria

class Inventory
{
    #Atributos

    code=0 #Codigo de producto (codigo de barras)
    description="" #Descripcion de producto(Marca,nombre,tipo[cerveza, vino, destilado,etc.] )
    stock=0 #Cantidad de producto en tienda
    price_sell=0 #Precio de venta (precio al cual se vende)
    price_buy=0 #Precio de compra (precio al cual se compra)
    total_sales=0 #Total de ventas (total  ganado en ventas)
    category[''] #Categoria de producto (alcohol,alimento,bebidas,etc)
    supplier="" #Proveedor (Coca cola company, PepsiCo,Brown-Forman Corporation)


    #Métodos

    show_data() #mostrar informacion
    add_description(newdescription) #Agregar descripción
    update_stock() #Actualizar stock en tienda
    update_pricesell() #Actualizar precio de venta
    update_pricebuy() #Actualizar precio de compra
    calculate_totalsales(profit) #Calcular total ganado en ventas
    add_category(newcategory) #Agregar categoria
    update_category() #actualizar categorias
    update_supplier() #Actualizar proveedor

}


class Product
{
    barcode=0 #Codigo de barras
    brand="" #Marca del poducto
    net_content=0 #Contenido neto del producto (en gramos si es alimento y ml si es bebestible)
    expiration_date=0 #Fecha de vencimiento

    update_barcode() #Actualizar codigo de barras
    add_brand() #Agregar marca del producto
    update_netcontent() #Actualizar contenido neto 
    add_expirationdate() #Agregar fecha de vencimiento 

} 
