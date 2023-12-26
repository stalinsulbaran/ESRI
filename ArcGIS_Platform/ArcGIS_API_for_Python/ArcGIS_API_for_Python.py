#!/usr/bin/env python
# coding: utf-8

# # Demo ArcGIS API for Python

# ## Importar ArcGIS API for Python

# In[ ]:


from arcgis.gis import GIS
from arcgis.features import FeatureLayerCollection
gis=GIS()


# ## Añadir un mapa

# In[ ]:


mapa=gis.map("Chile")
mapa.basemap = 'imagery'
mapa


# ## Buscar contenido

# In[ ]:


busqueda = gis.content.search('title: Satellite (VIIRS) Thermal Hotspots and Fire Activity',
                                    'Feature Layer')


# In[ ]:


incendios_capa = busqueda[0]
incendios_capa


# ## Visualizar el contendio en el mapa

# In[ ]:


mapa.add_layer(incendios_capa)
mapa

