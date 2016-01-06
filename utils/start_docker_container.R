# Certain packages (RCy3, RCytoscape, categoryCompare)
# require that certain java desktop apps (Cytoscape 2 or 3)
# be running. Each build needs its own instance of cytoscape.
# That means there need to be at least 8 instances altogether:
# linux + mavericks + snow leopard + win32 + win64 * (release + devel)
# (though snow leopard will be phased out soon)
# And each instance needs a significant amount of memory.
# Having all these instances running at once has proven to be
# problematic. They run as docker containers and soon consume
# all available memory.

# So this is a new approach. This script will be sourced
# by the packages above (only if they are running on the
# build system, not in ordinary end-user use) when the
# packages start a build or check, and this script
# will start a docker instance that will run for 40 minutes.

start_cytoscape_instance <- 
  function(calling_package, phase=c("buildsrc", "checksrc"), version=2,
    timeoutInMinutes=20)
 {
    if (missing(phase)) stop("phase must be buildsrc or checksrc!")
     if (version==2) 
     {
         hostvar <- "RCYTOSCAPE_HOST_OVERRIDE"
         portvar <- "RCYTOSCAPE_PORT_OVERRIDE"
         internalPort <- "9000"
         app <- "cytoscape"
     } else if (version==3) {
         hostvar <- "RCYTOSCAPE3_HOST_OVERRIDE"
         portvar <- "RCYTOSCAPE3_PORT_OVERRIDE"
         internalPort <- "1234"
         app <- "cytoscape3"
     } else 
        stop("version must be 2 or 3!")
     ssh <- Sys.getenv("BBS_SSH_CMD")
     ssh <- strsplit(ssh, " ")[[1]][1]
     host <- Sys.getenv(hostvar)
     port <- Sys.getenv(portvar)
     buildNode <- system2("hostname", stdout=TRUE)
     rsaKey <- Sys.getenv("BBS_RSAKEY")
     containerName <- sprintf("%s_%s_%s_%s",
        calling_package, app, phase, buildNode)
     # see if there is already a container running with this name:
     isRunning <- system2(ssh, sprintf("-i %s %s \"docker ps|grep -q %s\"",
        rsaKey, host, containerName))
     message(sprintf("Container already running? %s", as.character(isRunning == 0)))
     if (isRunning == 0) return(invisible(NULL))
     runCmd <- sprintf("-i %s %s \"nohup timeout %sm docker run -p %s:%s --rm --name %s dtenenba/%s > cytoscape_logs/%s.log 2>&1 &\"",
        rsaKey, host, timeoutInMinutes, port, internalPort,
        containerName,  app, containerName)
     cat(runCmd, "\n")
     result <- system2(ssh, runCmd)
 }
