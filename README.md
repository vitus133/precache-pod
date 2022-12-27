# precache-pod
This is an experiment for pre-caching container images on a kubernetes node using a pod. The pod creates a container for each image and pulls the image.
## How to use ##
To create the [pod spec](pod.yaml) from a [list of container images](images), use [create.py](create.py) script and a [template](pod-default.yaml):
```bash
$ ./create.py > pod.yaml
```
Then apply the pod to your cluster:
```bash
$ oc apply -f pod.yaml
```
The pod status will show error, as these are all arbitrary images:
```bash
$ oc get po

NAME           READY    STATUS      RESTARTS   AGE
test           25/183   Error       0          2d5h
```
I used [check.sh](check.sh) running on the node to verify all the images have been pre-cached.

## Ceveats ##
It's not clear what will happen in the case of disk pressure on the node. 
The kubelet should first garbage-collect the images, and only if this is not enough to 
alleviate the pressure condition it will start evicting pods.
It means, that if this pod is getting evicted, there is not enough space for pre-caching all the images
after GCing all the obsolete images.
