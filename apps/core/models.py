from django.db import models
from django.contrib.auth.models import User

class Titulo(models.Model):
    descripcion = models.CharField("DESCRIPCION", max_length=20, unique=True)
    descripcionReducida = models.CharField("ALIAS", max_length=5, blank=True)
    observacion = models.TextField("OBSERVACION", blank=True)
    #ultimoUsuario = models.ForeignKey(User, editable=False, on_delete=models.DO_NOTHING)
    #fechaCreacion = models.DateTimeField(auto_now_add=True)
    #fechaModificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.descripcion + " (" + self.descripcionReducida + ")"

    class Meta:
        ordering = ['descripcion']
        verbose_name_plural = "Titulos"

class TipoSexo(models.Model):
    descripcion = models.CharField("DESCRIPCION", max_length=20, unique=True)
    descripcionReducida = models.CharField("DESCRIPCION REDUCIDA", max_length=5, unique=True)
    observacion = models.TextField("OBSERVACION", blank=True)
    #ultimoUsuario = models.ForeignKey(User, editable=False, on_delete=models.DO_NOTHING)
    #fechaCreacion = models.DateTimeField(auto_now_add=True)
    #fechaModificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        ordering = ['descripcion']
        verbose_name_plural = "Tipos de sexo"
        verbose_name = "tipo de sexo"

class TipoDomicilio(models.Model):
    descripcion = models.CharField("DESCRIPCION", max_length=20, unique=True)
    descripcionReducida = models.CharField("DESCRIPCION REDUCIDA", max_length=5, unique=True)
    observacion = models.TextField("OBSERVACION", blank=True)
    #ultimoUsuario = models.ForeignKey(User, editable=False, on_delete=models.DO_NOTHING)
    #fechaCreacion= models.DateTimeField(auto_now_add=True)
    #fechaModificacion=models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return self.descripcion

    class Meta:
        ordering = ['descripcion']
        verbose_name_plural = "Tipos de domicilios"
        verbose_name = "tipo de domicilio"


class TipoDocumento(models.Model):
    descripcion = models.CharField("DESCRIPCION", max_length=20, unique=True)
    descripcionReducida = models.CharField("DESCRIPCION REDUCIDA", max_length=5, unique=True)
    observacion = models.TextField("OBSERVACION", blank=True)
    #ultimoUsuario = models.ForeignKey(User, editable=False, on_delete=models.DO_NOTHING)
    #fechaCreacion = models.DateTimeField(auto_now_add=True)
    #fechaModificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.descripcionReducida

    class Meta:
        ordering = ['descripcion']
        verbose_name_plural = "Tipos de documentos"
        verbose_name = "tipo de documento"


class Pais(models.Model):
    codigo = models.IntegerField("CODIGO", unique=True)
    codigoAlfa2 = descripcion = models.CharField("COD. 2 LETRAS", max_length=2)
    codigoAlfa3 = descripcion = models.CharField("COD. 3 LETRAS", max_length=3)
    descripcion = descripcion = models.CharField("DESCRIPCION", max_length=20)
    observacion = models.TextField("OBSERVACION", blank=True)
    #ultimoUsuario = models.ForeignKey(User, editable=False, on_delete=models.DO_NOTHING)
    #fechaCreacion = models.DateTimeField(auto_now_add=True)
    #fechaModificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        ordering = ['descripcion']
        verbose_name_plural = "Paises"


class Provincia(models.Model):
    codigo = models.CharField("LETRA DE PROV.", max_length=4)
    descripcion = models.CharField("DESCRIPCION", max_length=20)
    descripcionReducida = models.CharField("DESCRIPCION REDUCIDA", max_length=5, null=True)
    observacion = models.TextField("OBSERVACION", blank=True)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    #ultimoUsuario = models.ForeignKey(User, editable=False, on_delete=models.DO_NOTHING)
    #fechaCreacion = models.DateTimeField(auto_now_add=True, null=True)
    #fechaModificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        ordering = ['descripcion']
        unique_together = [("descripcion", "pais", "codigo")]


class Localidad(models.Model):
    codigo = models.CharField("CODIGO POSTAL", max_length=5)
    descripcion = models.CharField("DESCRIPCION", max_length=20)
    descripcionReducida = models.CharField("DESCRIPCION REDUCIDA", max_length=5, blank=True, null=True)
    observacion = models.TextField("OBSERVACION", blank=True, null=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT)
    #ultimoUsuario = models.ForeignKey(User, editable=False, null=True, on_delete=models.DO_NOTHING)
    #fechaCreacion = models.DateTimeField(auto_now_add=True, null=True)
    #fechaModificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.descripcion + " (" + self.provincia.descripcion + "-" + self.provincia.pais.codigoAlfa3 + ")"

    class Meta:
        unique_together = [("descripcion", "provincia", "codigo")]
        ordering = ['descripcion']
        verbose_name_plural = "Localidades"

class TipoTelefono(models.Model):
    descripcion = models.CharField("DESCRIPCION", max_length=20, unique=True)
    descripcionReducida = models.CharField("DESCRIPCION REDUCIDA", max_length=5, unique=True)
    observacion = models.TextField("OBSERVACION", blank=True)
    #ultimoUsuario = models.ForeignKey(User, editable=False, on_delete=models.DO_NOTHING)
    #fechaCreacion= models.DateTimeField(auto_now_add=True)
    #fechaModificacion=models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return self.descripcion

    class Meta:
        ordering = ['descripcion']
        verbose_name_plural = "Tipos de telefono"
        verbose_name = "tipo de telefono"

class TipoEstadoCivil(models.Model):
    descripcion = models.CharField("DESCRIPCION", max_length=20, unique=True)
    descripcionReducida = models.CharField("DESCRIPCION REDUCIDA", max_length=5, unique=True)
    observacion = models.TextField("OBSERVACION", blank=True)
    #ultimoUsuario = models.ForeignKey(User, editable=False, on_delete=models.DO_NOTHING)
    #fechaCreacion = models.DateTimeField(auto_now_add=True)
    #fechaModificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        ordering = ['descripcion']
        verbose_name_plural = "Tipos de estado civil"
        verbose_name = "tipo de estado civil"


class FactorSanguineo(models.Model):
    descripcion = models.CharField(max_length=1, unique=True)
    #ultimoUsuario = models.ForeignKey(User, editable=False,on_delete=models.DO_NOTHING)
    #fechaCreacion = models.DateTimeField(auto_now_add=True)
    #fechaModificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        ordering = ['descripcion']
        verbose_name_plural = "Factores Sanguineos"
        verbose_name = "factor sanguineo"

class GrupoSanguineo(models.Model):
    descripcion = models.CharField(max_length=2)
    factor = models.ForeignKey(FactorSanguineo, on_delete=models.PROTECT)
    #ultimoUsuario = models.ForeignKey(User, editable=False, on_delete=models.DO_NOTHING)
    #fechaCreacion = models.DateTimeField(auto_now_add=True)
    #fechaModificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.descripcion + "(" + self.factor.descripcion + ") "

    class Meta:
        unique_together = [("descripcion", "factor")]
        ordering = ['descripcion']
        verbose_name_plural = "Grupos Sanguineos"
        verbose_name = "grupo sanguineo"


class ObraSocial(models.Model):
    descripcion = models.CharField(max_length=100, unique=True)
    descripcion_reducida = models.CharField(max_length=4, unique=True)
    #ultimoUsuario = models.ForeignKey(User, editable=False, on_delete=models.DO_NOTHING)
    #fechaCreacion = models.DateTimeField(auto_now_add=True)
    #fechaModificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return "(" + self.descripcion_reducida + ") " + self.descripcion

    class Meta:
        ordering = ['descripcion_reducida']
        verbose_name_plural = "Obras Sociales"
        verbose_name = "obra social"



class Especialidad(models.Model):
    descripcion = models.CharField("DESCRIPCION", max_length=50)
    descripcionReducida = models.CharField("DESCRIPCION REDUCIDA", max_length=5, blank=True)
    observacion = models.TextField("OBSERVACION", blank=True)
    titulo = models.ForeignKey(Titulo, on_delete=models.PROTECT)
    #ultimoUsuario = models.ForeignKey(User, editable=False, on_delete=models.DO_NOTHING)
    #fechaCreacion= models.DateTimeField(auto_now_add=True)
    #fechaModificacion=models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return self.descripcion  +" ("+ self.titulo.descripcionReducida +")"

    class Meta:
        unique_together =[("descripcion","titulo")]
        ordering = ['descripcion']
        verbose_name_plural = "Especialidades"


class DatosProfesionales(models.Model):
    especialidad = models.ForeignKey(Especialidad, on_delete=models.DO_NOTHING)
    matriculap = models.CharField("Matricula Provincial", blank=True, max_length=10, )
    matriculan = models.CharField("Matricula Nacional", blank=True, max_length=10, )
    email = models.EmailField("Correo Electronico")
    #usuarioCreacion = models.ForeignKey(User, editable=False, related_name="creador_profesional", on_delete=models.DO_NOTHING)
    #usuarioModificacion = models.ForeignKey(User, editable=False, null=True, related_name="modificacdor_profesional", on_delete=models.DO_NOTHING)
    #ipCreacion = models.GenericIPAddressField(editable=False)
    #ipModificacion = models.GenericIPAddressField(editable=False, null=True)
    #fechaCreacion = models.DateTimeField(auto_now_add=True)
    #fechaModificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.especialidad)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Datos Profesionales"

class Telefono(models.Model):
    tipo_telefono = models.ForeignKey(TipoTelefono, on_delete=models.PROTECT)
    codigo_area = models.CharField("CODIGO DE AREA", max_length=20)
    numero = models.CharField("NUMERO TELEFONICO", max_length=20)
    observacion = models.TextField("OBSERVACION", blank=True)
    #usuarioCreacion = models.ForeignKey(User, editable=False, related_name="creador_telefono", on_delete=models.DO_NOTHING)
    #usuarioModificacion = models.ForeignKey(User, editable=False, null=True, related_name="modificacdor_telefono", on_delete=models.DO_NOTHING)
    #ipCreacion = models.GenericIPAddressField(editable=False)
    #ipModificacion = models.GenericIPAddressField(editable=False, null=True)
    #fechaCreacion = models.DateTimeField(auto_now_add=True)
    #fechaModificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.codigo_area + '-' + self.numero

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Telefonos"

class Domicilio(models.Model):
    tipo_domicilio = models.ForeignKey(TipoDomicilio, on_delete=models.PROTECT)
    direccion = models.CharField("DIRECCION", max_length=50)
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT)
    observacion = models.TextField("OBSERVACION", blank=True)
    #usuarioCreacion = models.ForeignKey(User, editable=False, related_name="creador_domicilio", on_delete=models.DO_NOTHING)
    #usuarioModificacion = models.ForeignKey(User, editable=False, null=True, related_name="modificacdor_domicilio", on_delete=models.DO_NOTHING)
    #ipCreacion = models.GenericIPAddressField(editable=False)
    #ipModificacion = models.GenericIPAddressField(editable=False, null=True)
    #fechaCreacion = models.DateTimeField(auto_now_add=True)
    #fechaModificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.direccion

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Domicilios"

class Persona(models.Model):
    nombre = models.CharField("NOMBRE", max_length=100)
    apellido = models.CharField("APELLIDO", max_length=100)
    sexo = models.ForeignKey(TipoSexo, on_delete=models.DO_NOTHING)
    estado_civil = models.ForeignKey(TipoEstadoCivil, on_delete=models.PROTECT)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.PROTECT, null=True)
    numero_documento = models.IntegerField(blank=True, null=True)
    grupo_sanguineo = models.ForeignKey(GrupoSanguineo, on_delete=models.PROTECT, null=True, blank=True)
    localidad_nacimiento = models.ForeignKey(Localidad, on_delete=models.PROTECT, null=True, blank=True)
    domicilio = models.ManyToManyField(Domicilio)#agregado posterior
    telefono = models.ManyToManyField(Telefono)#agregado posterior
    fecha_de_nacimiento = models.DateField("FECHA DE NACIMIENTO")
    datos_profesionales = models.ForeignKey(DatosProfesionales,related_name="personas", on_delete=models.PROTECT, null=True, blank=True)
    observacion = models.TextField("OBSERVACION", blank=True)
    #usuarioCreacion = models.ForeignKey(User, editable=False, related_name="creador_persona", on_delete=models.DO_NOTHING)
    #usuarioModificacion = models.ForeignKey(User, editable=False, null=True, related_name="modificacdor_persona", on_delete=models.DO_NOTHING)
    #ipCreacion = models.GenericIPAddressField(editable=False)
    #ipModificacion = models.GenericIPAddressField(editable=False, null=True)
    #fechaCreacion = models.DateTimeField(auto_now_add=True)
    #fechaModificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.apellido + ', ' + self.nombre + ' (' + str(self.tipo_documento.descripcionReducida) + ' ' + str(
            self.numero_documento) + ')'

    class Meta:
        # unique_together =[("tipo_documento","numero_documento")]
        ordering = ['-id']
        verbose_name_plural = "Personas"

class FotoPerfil(models.Model):
    foto = models.ImageField(upload_to='fotitos')
    persona = models.ForeignKey(Persona, on_delete=models.DO_NOTHING)
    #usuarioCreacion = models.ForeignKey(User, editable=False, related_name="creador_foto", on_delete=models.DO_NOTHING)
    #usuarioModificacion = models.ForeignKey(User, editable=False, null=True, related_name="modificacdor_foto", on_delete=models.DO_NOTHING)
    #ipCreacion = models.GenericIPAddressField(editable=False)
    #ipModificacion = models.GenericIPAddressField(editable=False, null=True)
    #fechaCreacion = models.DateTimeField(auto_now_add=True)
    #fechaModificacion = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = "Fotos de Perfil"

class ObraSocialDatos(models.Model):
    numero_afiliado = models.CharField("AFILIADO NRO", max_length=10)
    plan = models.CharField("PLAN", max_length=50)
    obra_social = models.ForeignKey(ObraSocial, on_delete=models.PROTECT)
    observacion = models.TextField("OBSERVACION", blank=True)
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    #usuarioCreacion = models.ForeignKey(User, editable=False, related_name="creador_obra_social", on_delete=models.DO_NOTHING)
    #usuarioModificacion = models.ForeignKey(User, editable=False, null=True, related_name="modificacdor_obra_social", on_delete=models.DO_NOTHING)
    #ipCreacion = models.GenericIPAddressField(editable=False)
    #ipModificacion = models.GenericIPAddressField(editable=False, null=True)
    #fechaCreacion = models.DateTimeField(auto_now_add=True)
    #fechaModificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.obra_social + 'Plan:' + self.plan + 'Afiliado Nro:' + self.numero_afiliado

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Obras Sociales Datos"


class CentroMedico(models.Model):
    descripcion = models.CharField("DESCRIPCION", max_length=50)
    descripcionReducida = models.CharField("DESCRIPCION REDUCIDA", max_length=5, blank=True)
    domicilio = models.ManyToManyField(Domicilio)#agregado posterior
    telefono = models.ManyToManyField(Telefono)#agregado posterior
    email = models.EmailField()
    #ultimoUsuario = models.ForeignKey(User, editable=False, on_delete=models.DO_NOTHING)
    #fechaCreacion= models.DateTimeField(auto_now_add=True)
    #fechaModificacion=models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        ordering = ['descripcion']
        verbose_name_plural = "Centros Medicos"