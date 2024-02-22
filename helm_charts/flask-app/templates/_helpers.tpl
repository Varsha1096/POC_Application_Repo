{{/* Define a template to generate a unique name for resources */}}
{{- define "flask-app.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name }}
{{- end -}}

{{/* Define a template to generate a unique name for the app */}}
{{- define "flask-app.name" -}}
{{- printf "%s-%s" .Release.Name "flask-app" }}
{{- end -}}
