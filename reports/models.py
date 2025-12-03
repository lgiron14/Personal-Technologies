from django.db import models

class Report(models.Model):
    """
    Representa un reporte general generado en el sistema.
    
    Puede contener archivos adjuntos y metadatos sobre su generación.
    """
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    generated_at = models.DateTimeField(auto_now_add=True, verbose_name="Generado el")
    file = models.FileField(upload_to='reports/', null=True, blank=True, verbose_name="Archivo Adjunto")

    class Meta:
        verbose_name = "Reporte"
        verbose_name_plural = "Reportes"

    def __str__(self):
        """Devuelve el título del reporte."""
        return self.title
