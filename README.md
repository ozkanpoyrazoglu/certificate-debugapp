# Certificate Checker App


This simple app checks your Kubernetes cluster's PKI certificates, and shows in a simple web ui. You can use it for checking certificate dates as debug tool.

Short description about PKI certificates from kubernetes.io
> Kubernetes requires PKI certificates for authentication over TLS. If you install Kubernetes with kubeadm, the certificates that your cluster requires are automatically generated. You can also generate your own certificates -- for example, to keep your private keys more secure by not storing them on the API server. 

More about PKI certficiates: https://kubernetes.io/docs/setup/best-practices/certificates/

## Main Features

- Cert-check app uses simple shell script, it shows end-dates with openssl. 
- It is working with volume mount in master node, that is because you should use this tool ephemerally.
- This repo contains simple shell script and python flask app.
- Python uses 5000 port, and you can create a service for that port.



## Installation

You can create a docker image, push to your registry (Docker-hub, Nexus, Artifactory or Amazon's ECR etc. ) and than create a simple deployment for your Kubernetes with that image.

For information about Docker build : https://docs.docker.com/engine/reference/commandline/build/

Certiface Checker app is working on master nodes in Kubernetes cluster. So you must set nodeSelector and tolerations in deployment definition for master nodes. For more information about [nodeselector](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) and [tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).
