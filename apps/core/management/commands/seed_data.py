from django.core.management.base import BaseCommand
from apps.transport.models import Transporte
from apps.services.models import ServicioTuristico
from apps.users.models import Usuario


class Command(BaseCommand):
    help = 'Puebla la base de datos con datos turísticos iniciales de Puntarenas'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Iniciando carga de datos iniciales...'))

        # Crear superusuario inicial si no existe
        if not Usuario.objects.filter(username='admin').exists():
            Usuario.objects.create_superuser(
                username='admin',
                email='admin@letsgo.cr',
                password='admin',
                first_name='Administrador',
                last_name='LetsGo'
            )
            self.stdout.write(self.style.SUCCESS('Superusuario creado: admin / admin'))

        # Crear transportes iniciales
        transportes_data = [
            # Bus
            {
                'nombre': 'Empresarios Unidos de Puntarenas (San José - Puntarenas)',
                'tipo': 'bus',
                'descripcion': 'Servicio directo y regular entre la Terminal de San José y el centro de Puntarenas por la Ruta 27.',
                'origen': 'Terminal San José (Calle 16, Ave 10/12)',
                'destino': 'Terminal Puntarenas (Paseo de los Turistas)',
                'horario': 'Salidas cada 40 minutos de 4:00 AM a 8:00 PM',
                'tarifa': '₡ 3,100 por persona',
                'empresa': 'Empresarios Unidos S.A.',
                'telefono': '+506 2222-0064',
                'whatsapp': '+506 8890-1234',
                'sitio_web': 'https://empresariosunidos.com',
            },
            {
                'nombre': 'Transportes Quepos - Puntarenas',
                'tipo': 'bus',
                'descripcion': 'Ruta costera por la Costanera Sur conectando Puntarenas con Jacó y Quepos/Manuel Antonio.',
                'origen': 'Terminal Central de Puntarenas',
                'destino': 'Quepos / Manuel Antonio',
                'horario': '4:30 AM, 10:30 AM y 3:00 PM diario',
                'tarifa': '₡ 2,800 por persona',
                'empresa': 'Transportes Quepos',
                'telefono': '+506 2777-0263',
            },
            {
                'nombre': 'Bus Urbano Chacarita - El Roble - Puntarenas Centro',
                'tipo': 'bus',
                'descripcion': 'Recorrido local que atraviesa la península desde el Hospital Monseñor Sanabria hasta el Faro.',
                'origen': 'El Roble / Barranca',
                'destino': 'Puntarenas Faro / Paseo de los Turistas',
                'horario': 'Salidas continuas cada 10-15 minutos de 5:00 AM a 10:00 PM',
                'tarifa': '₡ 450 pasaje regular',
                'empresa': 'Autotransportes El Roble',
                'telefono': '+506 2661-1234',
            },
            # Taxis
            {
                'nombre': 'Taxi Oficial Sitio Paseo de los Turistas',
                'tipo': 'taxi',
                'descripcion': 'Parada oficial de taxis rojos debidamente rotulados y regulados con taxímetro (María).',
                'origen': 'Paseo de los Turistas (Frente a los quioscos)',
                'destino': 'Todo Puntarenas, El Roble, Caldera y traslados al Aeropuerto',
                'horario': 'Servicio 24 horas',
                'tarifa': 'Tarifa regulada ARESEP (Tarifa inicial ₡ 750)',
                'empresa': 'Asociación de Taxistas del Puerto',
                'telefono': '+506 2661-0025',
                'whatsapp': '+506 8888-1122',
            },
            {
                'nombre': 'CoopeTaxi Puntarenas R.L.',
                'tipo': 'taxi',
                'descripcion': 'Servicio de radiotaxi y traslados ejecutivos por llamada o WhatsApp con unidades modernas con aire acondicionado.',
                'origen': 'Terminal de Buses / Muelle de Cruceros',
                'destino': 'Puntarenas y destinos interurbanos',
                'horario': '24/7 continuo',
                'tarifa': 'Tarifa estándar ARESEP con opción a tarifas fijas para tours',
                'empresa': 'CoopeTaxi Puntarenas',
                'telefono': '+506 2661-2020',
                'whatsapp': '+506 8333-4455',
            },
            # Tren
            {
                'nombre': 'Tren Turístico del Pacífico (Incofer)',
                'tipo': 'tren',
                'descripcion': 'Ruta histórica en tren que recorre los paisajes del Pacífico central hasta las cercanías del puerto.',
                'origen': 'Estación al Pacífico, San José',
                'destino': 'Estación Caldera / Puntarenas',
                'horario': 'Salidas especiales de fines de semana y temporada turística',
                'tarifa': '₡ 8,000 viaje redondo',
                'empresa': 'INCOFER',
                'telefono': '+506 2542-5800',
                'sitio_web': 'https://incofer.go.cr',
            },
            # Marítimo
            {
                'nombre': 'Ferry Coonatramar (Puntarenas - Playa Naranjo)',
                'tipo': 'maritimo',
                'descripcion': 'Cruce marítimo panorámico por el Golfo de Nicoya con transporte de pasajeros y vehículos.',
                'origen': 'Terminal Ferry Coonatramar, Puntarenas',
                'destino': 'Playa Naranjo',
                'horario': '6:30 AM, 10:00 AM, 2:30 PM, 7:30 PM',
                'tarifa': '₡ 1,000 adulto / ₡ 11,500 vehículo liviano',
                'empresa': 'Coonatramar R.L.',
                'telefono': '+506 2661-1069',
                'sitio_web': 'https://coonatramar.com',
            },
            {
                'nombre': 'Ferry Tambor (Puntarenas - Paquera)',
                'tipo': 'maritimo',
                'descripcion': 'Principal conexión marítima con la Península de Nicoya (Montezuma, Santa Teresa, Malpaís).',
                'origen': 'Muelle Terminal Ferry, Puntarenas Centro',
                'destino': 'Paquera',
                'horario': '5:30 AM, 9:00 AM, 12:00 PM, 3:00 PM, 6:00 PM, 8:30 PM',
                'tarifa': '₡ 950 adulto / ₡ 12,000 vehículo',
                'empresa': 'Naviera Tambor',
                'telefono': '+506 2661-2084',
                'sitio_web': 'https://navieratambor.com',
            },
            # Aéreo
            {
                'nombre': 'Vuelos Chárter & Aeródromo de Chacarita',
                'tipo': 'aereo',
                'descripcion': 'Conexiones chárter y vuelos privados para turistas hacia el Golfo de Nicoya, Quepos y Tambor.',
                'origen': 'Aeropuerto Internacional Juan Santamaría (SJO)',
                'destino': 'Aeródromo Chacarita / Pista Tambor',
                'horario': 'Vuelos bajo reserva y demanda diaria',
                'tarifa': 'Desde $120 por pasajero (según aeronave)',
                'empresa': 'Costa Rica Aero Charters',
                'telefono': '+506 2290-0000',
                'sitio_web': 'https://flycostarica.com',
            },
        ]

        for item in transportes_data:
            Transporte.objects.update_or_create(
                nombre=item['nombre'],
                defaults=item
            )
        self.stdout.write(self.style.SUCCESS(f'{len(transportes_data)} Medios de transporte registrados.'))

        # Crear servicios turísticos iniciales
        servicios_data = [
            # Rent a Car
            {
                'nombre': 'Puntarenas 4x4 & City Car Rental',
                'categoria': 'rentacar',
                'descripcion': 'Flota moderna de autos compactos, sedanes y camionetas 4x4 con kilometraje ilimitado y asistencia 24 horas en carretera.',
                'ubicacion': 'Frente a Playa Cocal, Puntarenas',
                'precio_desde': '$35 / día',
                'telefono': '+506 2663-1200',
                'whatsapp': '+506 8765-4321',
                'email': 'rentacar@puntarenas.cr',
                'destacado': True,
            },
            {
                'nombre': 'Costa Wheels Rent a Car',
                'categoria': 'rentacar',
                'descripcion': 'Entrega directa de vehículos en el muelle de cruceros y terminales de ferry sin costo adicional.',
                'ubicacion': 'Cerca del Muelle Principal de Cruceros',
                'precio_desde': '$40 / día',
                'telefono': '+506 2661-3400',
                'whatsapp': '+506 8555-9090',
                'email': 'reservas@costawheels.cr',
                'destacado': False,
            },
            # Acuático
            {
                'nombre': 'Puntarenas Wave & Jet Ski Adventures',
                'categoria': 'acuatico',
                'descripcion': 'Alquiler de motos de agua (Jet Ski), paseos en banana boat, tablas de paddleboard y kayaks para recorrer la bahía.',
                'ubicacion': 'Playa Puntarenas (Sector El Faro)',
                'precio_desde': '$50 / 30 minutos',
                'telefono': '+506 8899-7766',
                'whatsapp': '+506 8899-7766',
                'email': 'waves@puntarenas.cr',
                'destacado': True,
            },
            {
                'nombre': 'Boca Barranca Surf & Paddle Club',
                'categoria': 'acuatico',
                'descripcion': 'Clases profesionales de surf en una de las olas izquierdas más famosas del mundo. Alquiler de tablas de fibra y foam.',
                'ubicacion': 'Boca Barranca, Puntarenas',
                'precio_desde': '$30 / clase o alquiler por día',
                'telefono': '+506 8321-4567',
                'email': 'surf@bocabarranca.cr',
                'destacado': False,
            },
            # Hospedaje
            {
                'nombre': 'Hotel Tioga Puntarenas',
                'categoria': 'hospedaje',
                'descripcion': 'Hotel tradicional con ubicación privilegiada en pleno Paseo de los Turistas frente a la playa, piscinas y restaurante de mariscos.',
                'ubicacion': 'Paseo de los Turistas, Calles 17 y 19, Puntarenas',
                'precio_desde': '₡ 45,000 / noche con desayuno',
                'telefono': '+506 2661-0271',
                'whatsapp': '+506 8812-3456',
                'email': 'info@hoteltioga.com',
                'sitio_web': 'https://hoteltioga.com',
                'destacado': True,
            },
            {
                'nombre': 'Puerto Azul Boutique Resort & Marina',
                'categoria': 'hospedaje',
                'descripcion': 'Exclusivo complejo hotelero y marina en el estero de Puntarenas. Suites de lujo, piscinas infinitas, spa y restaurante internacional.',
                'ubicacion': 'Barrio El Cocal, Puntarenas',
                'precio_desde': '₡ 75,000 / noche',
                'telefono': '+506 2661-4000',
                'whatsapp': '+506 8900-1122',
                'email': 'reservas@puertoazulresort.com',
                'sitio_web': 'https://puertoazulresort.com',
                'destacado': True,
            },
            {
                'nombre': 'Cabinas San Isidro',
                'categoria': 'hospedaje',
                'descripcion': 'Cómodas cabinas familiares completamente equipadas con cocina, refrigerador, aire acondicionado y piscina familiar.',
                'ubicacion': 'San Isidro de Puntarenas',
                'precio_desde': '₡ 22,000 / noche',
                'telefono': '+506 2663-0031',
                'destacado': False,
            },
            # Tours
            {
                'nombre': 'Tour de un Día en Catamarán a Isla Tortuga',
                'categoria': 'tour',
                'descripcion': 'Aventura inolvidable por el Golfo de Nicoya hacia Isla Tortuga con snorkel, música, barra libre de bebidas naturales y delicioso almuerzo en la playa.',
                'ubicacion': 'Salida desde el Muelle de Puntarenas',
                'precio_desde': '$85 por persona',
                'telefono': '+506 2661-5500',
                'whatsapp': '+506 8661-5500',
                'email': 'tours@islatortugacr.com',
                'sitio_web': 'https://islatortugacr.com',
                'destacado': True,
            },
            {
                'nombre': 'Safari en Manglar y Avistamiento de Aves del Estero',
                'categoria': 'tour',
                'descripcion': 'Recorrido ecológico en lancha por los canales de manglares del Estero de Puntarenas para observar aves acuáticas, garzas, monos y cocodrilos.',
                'ubicacion': 'Estero de Puntarenas',
                'precio_desde': '$35 por persona',
                'telefono': '+506 8456-7890',
                'whatsapp': '+506 8456-7890',
                'destacado': True,
            },
        ]

        for item in servicios_data:
            ServicioTuristico.objects.update_or_create(
                nombre=item['nombre'],
                defaults=item
            )
        self.stdout.write(self.style.SUCCESS(f'{len(servicios_data)} Servicios turísticos registrados.'))
        self.stdout.write(self.style.SUCCESS('¡Carga de datos completada exitosamente!'))
