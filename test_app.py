apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: cicd-final-project
spec:
  to:
    kind: Service
    name: cicd-final-project
  port:
    targetPort: 8080
