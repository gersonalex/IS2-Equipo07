# === Importamos las vistas basadas en clases y en funciones del codigo fuente de views.py ===
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from apps.rol.views import crear_rol_view_sistema, lista_rol, search, editar_rol, eliminar_rol, asignar_rol_usuario
from apps.rol.views import crear_rol_view, rol_opciones_sistema, ListaRol_sistema, EditarRol_sistema, \
    EliminarRol_sistema, search_sistema, Usuario_roles

# **Vistas**


# **1.lista :** Vista que despliega la lista de roles existentes en el sistema<br/>
# **2.eliminar rol :** Vista que despliega eliminar un rol<br/>
# **3.crear rol :** Vista que despliega la definición de un rol<br/>
# **4.modificar rol :** Vista que despliega modificar un rol<br/>
# **5.search :** Vista que despliega una lista de roles buscados.<br/>
urlpatterns = [
    # ** Dirección de URL desplegar las vistas en la dirección de plantillas respectivamente. **

    url(r'^lista/(?P<id_fase>\d+)/$', login_required(lista_rol), name='rol_lista'),
    url(r'^eliminar-rol/(?P<pk>\d+)/(?P<id_fase>\d+)/$', login_required(eliminar_rol), name='rol_eliminar'),
    url(r'^crear/(?P<id_fase>\d+)/$', login_required(crear_rol_view), name='rol_crear'),
    url(r'^modificar-rol/(?P<pk>\d+)/(?P<id_fase>\d+)/$', login_required(editar_rol), name='rol_editar'),
    url(r'^results/(?P<id_fase>\d+)/$', login_required(search), name='search'),
    url(r'^asignar/(?P<pk>\d+)/(?P<id_fase>\d+)/$', login_required(asignar_rol_usuario), name='rol_asignar_usuario'),
    #=== ROL SISTEMA ===
    url(r'^opciones/', login_required(permission_required('rol.gestion_rol_sistema', raise_exception=True)(rol_opciones_sistema)), name='rol_opciones_sistema'),
    url(r'^lista/', login_required(permission_required('rol.listar_rol_sistema', raise_exception=True)(ListaRol_sistema.as_view())), name='rol_lista_sistema'),
    url(r'^results/$', login_required(permission_required('rol.listar_rol_sistema', raise_exception=True)(search_sistema)), name='search_sistema'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(permission_required('rol.eliminar_rol_sistema', raise_exception=True)(EliminarRol_sistema.as_view())), name='rol_eliminar_sistema'),
    url(r'^crear/', login_required(permission_required('rol.crear_rol_sistema', raise_exception=True)(crear_rol_view_sistema)), name='rol_crear_sistema'),
    url(r'^modificar/(?P<pk>\d+)/$', login_required(permission_required('rol.editar_rol_sistema', raise_exception=True)(EditarRol_sistema.as_view(model=Group, ))), name='rol_editar_sistema'),
    
    url(r'^usuario-roles/', login_required(Usuario_roles.as_view()), name='usuario_rol'),
    # === FIN ====
]

# === Indice de la documentación de la Aplicación rol  === <br/>
# 1.apps     : [[apps.py]]<br/>
# 2.forms    : [[forms.py]]<br/>
# 3.tests    : [[tests.py]]<br/>
# 4.urls     : [[urls.py]]<br/>
# 5.views    : [[views.py]]<br/>

# Regresar al menu principal : [Menú Principal](../../docs-index/index.html)
