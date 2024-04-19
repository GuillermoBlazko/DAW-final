# DAW-FINAL-BACKEND

## Proyecto Final: Desarrollo de una Red Social basada en Geolocalización

Este proyecto consiste en el desarrollo de una red social que utiliza la geolocalización para mostrar mensajes que estén cerca del usuario. A diferencia de las redes sociales convencionales que presentan un feed estático, esta plataforma busca enriquecer la experiencia del usuario al proporcionar mensajes contextualizados según su ubicación física.

### Características principales:

- **Geolocalización**: Utiliza la ubicación del usuario para determinar los mensajes relevantes en su área cercana.

### Historial de Desarrollo:

- **18/08/24**:
  - Añadida la funcionalidad de enviar y recibir mensajes con geolocalización incorporada.
  - Base de datos mudada a una AWS RDS PostgreSQL con una caché en ElastiCache para ayudar con latencia.
  - Creación de un bucket S3 para gestionar imágenes de la aplicación.
- **19/08/24**:
  - Eliminado un bug que enviaba múltiples mensajes simultáneamente.
  - Eliminado un bug que permitía enviar mensajes completamemente vacíos.
  - Eliminado un bug en el cual la triangulación de la posición se guardaba como 0 provocando problemas en la visualización de mensajes
  - Eliminado un bug en el que se enviaban mensajes con inyeccion HTML. 
  - Nueva página de login con nuevas validaciones tanto en back como en frontend. 

