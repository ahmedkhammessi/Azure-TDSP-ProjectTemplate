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
    print('Cluster already exists.')
except ComputeTargetException:
    compute_config = AmlCompute.provisioning_configuration(vm_size='Standard_NC6', max_nodes=4)
    cpu_cluster = AmlCompute.create(ws,cpu_cluster_name,compute_config)

cpu_cluster.wait_for_completion(show_output=True)