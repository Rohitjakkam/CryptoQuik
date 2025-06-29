#!/bin/bash


echo "RUNNING Create Cluster and Intall Kafka and Kafka UI..."
cd deployments/dev/kind # Go to the kind directory
chmod +x create_cluster.sh # Make the script executable
./create_cluster.sh # Run the script