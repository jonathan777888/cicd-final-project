apiVersion: v1
kind: Service
metadata:
  name: cicd-final-project
spec:
  selector:
    app: cicd-final-project
  ports:
    - protocol: TCP
      port: 8080
      targetPort: 8080
