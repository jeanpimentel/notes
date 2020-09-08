# Jenkins - List installed plugins



Go to Script console, `http://<your-jenkins-server>/script`

```scala
jenkins.model.Jenkins.instance.getPluginManager().getPlugins().stream().sorted().each { 
	println "${it.getShortName()} | ${it.getVersion()} | ${it.getDisplayName()}" 
}
```

