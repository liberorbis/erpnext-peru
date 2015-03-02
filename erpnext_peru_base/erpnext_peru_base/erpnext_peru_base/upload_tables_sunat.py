# -*- coding: utf-8 -*-
# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals

import frappe

from frappe import _


from frappe import _
def tables_sunat_after_install():
    install_docs = [

        {'doctype':'table_sunat', 'name':'TABLAS_SUNAT','field_name':'TABLAS_SUNAT','table_code':'TABLAS_SUNAT', 'active':1},
        #TABLE 01 - SUNAT

         {'doctype':'Table Sunat 01', 'name':'TIPOS DE MEDIO DE PAGO','field_name':'TIPOS DE MEDIO DE PAGO','code':'TABLA_1', 'active':1,'parent_table_sunat':_('TABLAS_SUNAT'),
         'element_tables':[
             {'name':'DEPOSITO EN CUENTA', 'element_code':'001', 'element_code2':'','field_name':'DEPOSITO EN CUENTA', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,'table_sunat':_('TIPOS DE MEDIO DE PAGO'),},
             {'name':'TRANSFERENCIA DE FONDOS', 'element_code':'003', 'element_code2':'','field_name':'TRANSFERENCIA DE FONDOS', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,'table_sunat':_('TIPOS DE MEDIO DE PAGO'),},
             {'name':'ORDEN DE PAGO', 'element_code':'004', 'element_code2':'','field_name':'ORDEN DE PAGO', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,'table_sunat':_('TIPOS DE MEDIO DE PAGO'),},
             {'name':'TARJETA DE DÉBITO', 'element_code':'005', 'element_code2':'','field_name':'TARJETA DE DÉBITO', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,'table_sunat':_('TIPOS DE MEDIO DE PAGO'),},
             {'name':'TARJETA DE CREDITO', 'element_code':'006', 'element_code2':'','field_name':'TARJETA DE CREDITO', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,'table_sunat':_('TIPOS DE MEDIO DE PAGO'),},
             {'name':'CHEQUE NO NEGOCIABLE', 'element_code':'007', 'element_code2':'','field_name':'CHEQUE NO NEGOCIABLE', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'CHEQUES CON LA CLÁUSULA DE <<NO NEGOCIABLE>>, <<INTRANSFERIBLES>>, <<NO A LA ORDEN>> U OTRA EQUIVALENTE, A QUE SE REFIERE EL INCISO F) DEL ARTICULO 5° DEL DECRETO LEGISLATIVO.','active':1,'table_sunat':_('TIPOS DE MEDIO DE PAGO'),},
             {'name':'EFECTIVO,NO OLIGADO A MEDIOS DE PAGO', 'element_code':'008', 'element_code2':'','field_name':'EFECTIVO,NO OLIGADO A MEDIOS DE PAGO', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'EFECTIVO, EN LOS DEMÁS CASOS','active':1,'table_sunat':_('TIPOS DE MEDIO DE PAGO'),},
             {'name':'EFECTIVO', 'element_code':'009', 'element_code2':'','field_name':'EFECTIVO', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'EFECTIVO, EN LOS DEMÁS CASOS','active':1,'table_sunat':_('TIPOS DE MEDIO DE PAGO'),},
             {'name':'MEDIOS DE PAGO DE COMERCIO EXTERIOR', 'element_code':'010', 'element_code2':'','field_name':'MEDIOS DE PAGO DE COMERCIO EXTERIOR', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,'table_sunat':_('TIPOS DE MEDIO DE PAGO'),},
             {'name':'LETRAS DE CAMBIO', 'element_code':'011', 'element_code2':'','field_name':'LETRAS DE CAMBIO', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,'table_sunat':_('TIPOS DE MEDIO DE PAGO'),},
             {'name':'TRANSFERENCIAS - COMERCIO EXTERIOR', 'element_code':'101', 'element_code2':'','field_name':'TRANSFERENCIAS - COMERCIO EXTERIOR', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,'table_sunat':_('TIPOS DE MEDIO DE PAGO'),},
             {'name':'CHEQUES BANCARIOS - COMERCIO EXTERIOR', 'element_code':'102', 'element_code2':'','field_name':'CHEQUES BANCARIOS - COMERCIO EXTERIOR', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,'table_sunat':_('TIPOS DE MEDIO DE PAGO'),},
             {'name':'ORDEN DE PAGO SIMPLE - COMERCIO EXTERIOR', 'element_code':'103', 'element_code2':'','field_name':'ORDEN DE PAGO SIMPLE - COMERCIO EXTERIOR', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,'table_sunat':_('TIPOS DE MEDIO DE PAGO'),},
             {'name':'ORDEN DE PAGO DOCUMENTARIO - COMERCIO EXTERIOR', 'element_code':'104', 'element_code2':'','field_name':'ORDEN DE PAGO DOCUMENTARIO - COMERCIO EXTERIOR', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,'table_sunat':_('TIPOS DE MEDIO DE PAGO'),},
             {'name':'REMESA SIMPLE - COMERCIO EXTERIOR', 'element_code':'105','element_code2':'','field_name':'REMESA SIMPLE - COMERCIO EXTERIOR', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,'table_sunat':_('TIPOS DE MEDIO DE PAGO'),},
             {'name':'REMESA DOCUMENTARIA - COMERCIO EXTERIOR', 'element_code':'106','element_code2':'','field_name':'REMESA DOCUMENTARIA - COMERCIO EXTERIOR', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,'table_sunat':_('TIPOS DE MEDIO DE PAGO'),},
             {'name':'CARTA DE CREDITO SIMPLE - COMERCIO EXTERIOR', 'element_code':'107','element_code2':'','field_name':'CARTA DE CREDITO SIMPLE - COMERCIO EXTERIOR', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,'table_sunat':_('TIPOS DE MEDIO DE PAGO'),},
             {'name':'CARTA DE CREDITO DOCUMENTARIO - COMERCIO EXTERIOR', 'element_code':'108','element_code2':'','field_name':'CARTA DE CREDITO DOCUMENTARIO - COMERCIO EXTERIOR', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,'table_sunat':_('TIPOS DE MEDIO DE PAGO'),},
             {'name':'OTROS MEDIOS DE PAGO (ESPECIFICAR)', 'element_code':'999','element_code2':'','field_name':'OTROS MEDIOS DE PAGO (ESPECIFICAR)', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,'table_sunat':_('TIPOS DE MEDIO DE PAGO'),},
         ]
         },
         #TABLE 02 - SUNAT
        #{'doctype':'table_sunat', 'name':'TIPOS DE DOCUMENTO DE IDENTIDAD','field_name':'TIPOS DE DOCUMENTO DE IDENTIDAD','table_code':'TABLA_2', 'active':1,'parent_table_sunat':_('TABLAS_SUNAT')},
        {'doctype':'Table Sunat 02', 'name':'TIPOS DE MEDIO DE PAGO','field_name':'TIPOS DE MEDIO DE PAGO','code':'TABLA_1', 'active':1,'parent_table_sunat':_('TABLAS_SUNAT'),
         'element_tables':[
             {'name':'OTROS TIPOS DE DOCUMENTOS', 'element_code':'0','element_code2':'','field_name':'REMESA SIMPLE - COMERCIO EXTERIOR', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'DNI', 'element_code':'01','element_code2':'','field_name':'DNI', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'DOCUMENTO NACIONAL DE IDENTIDAD','active':1,},
             {'name':'CARNET DE EXTRANJERIA', 'element_code':'04','element_code2':'','field_name':'CARNET DE EXTRANJERIA', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'RUC', 'element_code':'06','element_code2':'','field_name':'RUC', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'REGISTRO UNICO DE CONTRIBUYENTES','active':1,},
             {'name':'PASAPORTE', 'element_code':'07','element_code2':'','field_name':'PASAPORTE', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
         ]
         },
        #TABLE 12 - SUNAT
        #{'doctype':'table_sunat', 'name':'TIPO DE OPERACION','field_name':'TIPO DE OPERACION','table_code':'TABLA_12', 'active':1,'parent_table_sunat':_('TABLAS_SUNAT')},
         {'doctype':'Table Sunat 12', 'name':'TIPOS DE MEDIO DE PAGO','field_name':'TIPOS DE MEDIO DE PAGO','code':'TABLA_1', 'active':1,'parent_table_sunat':_('TABLAS_SUNAT'),
         'element_tables':[
             {'name':'VENTA', 'element_code':'01','element_code2':'','field_name':'VENTA', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'COMPRA', 'element_code':'02','element_code2':'','field_name':'COMPRA', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'DOCUMENTO NACIONAL DE IDENTIDAD','active':1,},
             {'name':'CONSIGNACIÓN RECIBIDA', 'element_code':'03','element_code2':'','field_name':'CONSIGNACIÓN RECIBIDA', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'CONSIGNACIÓN ENTREGADA', 'element_code':'04','element_code2':'','field_name':'CONSIGNACIÓN ENTREGADA', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'DEVOLUCIÓN RECIBIDA', 'element_code':'05','element_code2':'','field_name':'DEVOLUCIÓN RECIBIDA', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'DEVOLUCIÓN ENTREGADA', 'element_code':'06','element_code2':'','field_name':'DEVOLUCIÓN ENTREGADA', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'PROMOCIÓN', 'element_code':'07','element_code2':'','field_name':'PROMOCIÓN', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'PREMIO', 'element_code':'08','element_code2':'','field_name':'PREMIO', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'DONACIÓN', 'element_code':'09','element_code2':'','field_name':'DONACIÓN', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'SALIDA A PRODUCCIÓN', 'element_code':'10','element_code2':'','field_name':'SALIDA A PRODUCCIÓN', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'TRANSFERENCIA ENTRE ALMACENES', 'element_code':'11','element_code2':'','field_name':'TRANSFERENCIA ENTRE ALMACENES', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'RETIRO', 'element_code':'12','element_code2':'','field_name':'RETIRO', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'MERMAS', 'element_code':'13','element_code2':'','field_name':'MERMAS', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'DESMEDROS', 'element_code':'14','element_code2':'','field_name':'DESMEDROS', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'DESTRUCCIÓN', 'element_code':'15','element_code2':'','field_name':'DESTRUCCIÓN', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'SALDO INICIAL', 'element_code':'16','element_code2':'','field_name':'SALDO INICIAL', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'OTROS (ESPECIFICAR)', 'element_code':'99','element_code2':'','field_name':'OTROS (ESPECIFICAR)', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
         ]
         },
        #TABLE 10 - SUNAT
        #{'doctype':'table_sunat', 'name':'TIPO DE COMPROBANTE DE PAGO O DOCUMENTO','field_name':'TIPO DE COMPROBANTE DE PAGO O DOCUMENTO','table_code':'TABLA_10', 'active':1,'parent_table_sunat':_('TABLAS_SUNAT')},
        {'doctype':'Table Sunat 10', 'name':'TIPOS DE MEDIO DE PAGO','field_name':'TIPOS DE MEDIO DE PAGO','code':'TABLA_1', 'active':1,'parent_table_sunat':_('TABLAS_SUNAT'),
         'element_tables':[
             {'name':'Otros(especificar)', 'element_code':'00','element_code2':'','field_name':'Otros(especificar)', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Factura', 'element_code':'01','element_code2':'','field_name':'Factura', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Recibo por Honorarios', 'element_code':'02','element_code2':'','field_name':'Recibo por Honorarios', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Boleta de Venta', 'element_code':'03','element_code2':'','field_name':'Boleta de Venta', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Liquidación de compra', 'element_code':'04','element_code2':'','field_name':'Liquidación de compra', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Boleto aviación comercial', 'element_code':'05','element_code2':'','field_name':'Boleto aviación comercial', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'Boleto de compañía de aviación comercial por el servicio de transporte aéreo de pasajeros','active':1,},
             {'name':'Carta de porte aéreo', 'element_code':'06','element_code2':'','field_name':'Carta de porte aéreo', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'Carta de porte aéreo por el servicio de transporte de carga aérea','active':1,},
             {'name':'Nota de crédito', 'element_code':'07','element_code2':'','field_name':'Nota de crédito', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Nota de débito', 'element_code':'08','element_code2':'','field_name':'Nota de débito', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Guía de remisión - Remitente', 'element_code':'09','element_code2':'','field_name':'Guía de remisión - Remitente', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Recibo por Arrendamiento', 'element_code':'10','element_code2':'','field_name':'Recibo por Arrendamiento', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Póliza emitidas', 'element_code':'11','element_code2':'','field_name':'Póliza emitidas', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'Póliza emitida por las Bolsas de Valores, Bolsas de Productos o Agentes de Intermediación por operaciones, realizadas en las Bolsas de Valores o Productos o fuera de las mismas, autorizadas por CONASEV','active':1,},
             {'name':'Ticket o cinta emitido por máquina registradora', 'element_code':'12','element_code2':'','field_name':'Ticket o cinta emitido por máquina registradora', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Documento emitido por bancos, instituciones financieras, crediticias y de seguros (controlados por SBS)', 'element_code':'13','element_code2':'','field_name':'Documento emitido por bancos, instituciones financieras, crediticias y de seguros (controlados por SBS)', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'Documento emitido por bancos, instituciones financieras, crediticias y de seguros que se encuentren bajo el,control de la Superintendencia de Banca y Seguros','active':1,},
             {'name':'Recibo servicios públicos', 'element_code':'14','element_code2':'','field_name':'Recibo servicios públicos', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'Recibo por servicios públicos de suministro de energía eléctrica, agua, teléfono, telex y telegráficos y otros servicios complementarios que se incluyan en el recibo de servicio público','active':1,},
             {'name':'Boleto emitido por las empresas de transporte público urbano de pasajeros', 'element_code':'15','element_code2':'','field_name':'Boleto emitido por las empresas de transporte público urbano de pasajeros', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Boleto de viaje emitido por las empresas de transporte público interprovincial de pasajeros dentro del país', 'element_code':'16','element_code2':'','field_name':'Boleto de viaje emitido por las empresas de transporte público interprovincial de pasajeros dentro del país', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Documento emitido por la Iglesia Católica por el arrendamiento de bienes inmuebles', 'element_code':'17','element_code2':'','field_name':'Documento emitido por la Iglesia Católica por el arrendamiento de bienes inmuebles', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Documento emitido por las Administradoras Privadas de Fondo de Pensiones', 'element_code':'18','element_code2':'','field_name':'Documento emitido por las Administradoras Privadas de Fondo de Pensiones', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'Documento emitido por las Administradoras Privadas de Fondo de Pensiones que se encuentran bajo la supervisión de la Superintendencia de Administradoras Privadas de Fondos de Pensiones','active':1,},
             {'name':'Boleto o entrada por atracciones y espectáculos públicos', 'element_code':'19','element_code2':'','field_name':'Boleto o entrada por atracciones y espectáculos públicos', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Comprobante de Retención', 'element_code':'20','element_code2':'','field_name':'Comprobante de Retención', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Conocimiento de embarque por el servicio de transporte de carga marítima', 'element_code':'21','element_code2':'','field_name':'Conocimiento de embarque por el servicio de transporte de carga marítima', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Comprobante por Operaciones No Habituales', 'element_code':'22','element_code2':'','field_name':'Comprobante por Operaciones No Habituales', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Pólizas de adjudicaciones', 'element_code':'23','element_code2':'','field_name':'Pólizas de adjudicaciones', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'Pólizas de Adjudicación emitidas con ocasión del remate o adjudicación de bienes por venta forzada, por los martilleros o las entidades que rematen o subasten bienes por cuenta de terceros','active':1,},
             {'name':'Certificado de pago de regalías emitidas por PERUPETRO S.A', 'element_code':'24','element_code2':'','field_name':'Certificado de pago de regalías emitidas por PERUPETRO S.A', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Documento de atribución', 'element_code':'25','element_code2':'','field_name':'Documento de atribución', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'Documento de Atribución (Ley del Impuesto General a las Ventas e Impuesto Selectivo al Consumo, Art. 19º, último párrafo, R.S. N° 022-98-SUNAT).','active':1,},
             {'name':'Recibo por el Pago de la Tarifa por Uso de Agua Superficial', 'element_code':'26','element_code2':'','field_name':'Recibo por el Pago de la Tarifa por Uso de Agua Superficial', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'Recibo por el Pago de la Tarifa por Uso de Agua Superficial con fines agrarios y por el pago de la Cuota para la ejecución de una determinada obra o actividad acordada por la Asamblea General de la Comisión de Regantes o Resolución expedida por el Jefe de la Unidad de Aguas y de Riego (Decreto Supremo N° 003-90-AG, Arts. 28 y 48)','active':1,},
             {'name':'Seguro Complementario de Trabajo de Riesgo', 'element_code':'27','element_code2':'','field_name':'Seguro Complementario de Trabajo de Riesgo', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Tarifa Unificada de Uso de Aeropuerto', 'element_code':'28','element_code2':'','field_name':'Tarifa Unificada de Uso de Aeropuerto', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Documentos emitidos por la COFOPRI en calidad de oferta de venta de terrenos', 'element_code':'29','element_code2':'','field_name':'Documentos emitidos por la COFOPRI en calidad de oferta de venta de terrenos', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'Documentos emitidos por la COFOPRI en calidad de oferta de venta de terrenos, los correspondientes a las subastas públicas y a la retribución de los servicios que presta','active':1,},
             {'name':'Doc. empresas rol de adguiriente en los sistemas de pago', 'element_code':'30','element_code2':'','field_name':'Doc. empresas rol de adguiriente en los sistemas de pago', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'Documentos emitidos por las empresas que desempeñan el rol adquirente en los sistemas de pago mediante tarjetas de crédito o débito','active':1,},
             {'name':'Guía de Remisión - Transportista', 'element_code':'31','element_code2':'','field_name':'Guía de Remisión - Transportista', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Doc. Garantia de red principal', 'element_code':'32','element_code2':'','field_name':'Doc. Garantia de red principal', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'Documentos emitidos por las empresas recaudadoras de la denominada Garantía de Red Principal a la que hace referencia ','active':1,},
             {'name':'Documento del Operador', 'element_code':'34','element_code2':'','field_name':'Documento del Operador', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Documento del Partícipe', 'element_code':'35','element_code2':'','field_name':'Documento del Partícipe', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Recibo de Distribución de Gas Natural', 'element_code':'36','element_code2':'','field_name':'Recibo de Distribución de Gas Natural', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Doc. por servicios de consecionarios', 'element_code':'37','element_code2':'','field_name':'Doc. por servicios de consecionarios', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'Documentos que emitan los concesionarios del servicio de revisiones técnicas vehiculares, por la prestación de dicho servicio','active':1,},
             {'name':'Constancia de Depósito - IVAP (Ley 28211)', 'element_code':'40','element_code2':'','field_name':'Constancia de Depósito - IVAP (Ley 28211)', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Declaración Única de Aduanas - Importación definitiva', 'element_code':'50','element_code2':'','field_name':'Declaración Única de Aduanas - Importación definitiva', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Despacho Simplificado - Importación Simplificada', 'element_code':'52','element_code2':'','field_name':'Despacho Simplificado - Importación Simplificada', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Declaración de Mensajería o Courier', 'element_code':'53','element_code2':'','field_name':'Declaración de Mensajería o Courier', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Liquidación de Cobranza', 'element_code':'54','element_code2':'','field_name':'Liquidación de Cobranza', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'BVME para transporte ferroviario de pasajeros', 'element_code':'55','element_code2':'','field_name':'BVME para transporte ferroviario de pasajeros', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Comprobante de pago SEAE', 'element_code':'56','element_code2':'','field_name':'Comprobante de pago SEAE', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Nota de Crédito Especial', 'element_code':'87','element_code2':'','field_name':'Nota de Crédito Especial', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Nota de Débito Especial', 'element_code':'88','element_code2':'','field_name':'Nota de Débito Especial', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Comprobante de No Domiciliado', 'element_code':'91','element_code2':'','field_name':'Comprobante de No Domiciliado', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Exceso de crédito fiscal por retiro de bienes', 'element_code':'96','element_code2':'','field_name':'Exceso de crédito fiscal por retiro de bienes', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Nota de Crédito - No Domiciliado', 'element_code':'97','element_code2':'','field_name':'Nota de Crédito - No Domiciliado', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
             {'name':'Nota de Débito - No Domiciliado', 'element_code':'98','element_code2':'','field_name':'Nota de Débito - No Domiciliado', 'val_porcent':0,'val_float':0,'val_string':'','desciption':'','active':1,},
         ]
         },
	]
    from frappe.modules import scrub
    for r in install_docs:
		doc = frappe.new_doc(r.get("doctype"))
		doc.update(r)

		# ignore mandatory for root
		parent_link_field = ("parent_" + scrub(doc.doctype))
		if doc.meta.get_field(parent_link_field) and not doc.get(parent_link_field):
			doc.ignore_mandatory = True

		doc.insert()
