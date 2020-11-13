from azureml.core import Workspace
from azureml.core.compute import ComputeTarget, AmlCompute
from azureml.core.compute_target import ComputeTargetException

ws = Workspace.get(name='akws', 
                   subscription_id='8b3748c0-bb0b-4913-ab5b-c462062118fe',
                   resource_group='akrg')

cpu_cluster_name = 'tdsp-cluster'

#verify that cluster does not exist
try:
    cpu_cluster = AmlCompute(workspace=ws, name=cpu_cluster_name)
    cpu_cluster.delete()
    print('Deleting cluster...')
except ComputeTargetException:
    print('Cluster does not exist in workspace.')