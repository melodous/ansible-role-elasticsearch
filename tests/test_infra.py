import pytest

def test_elasticsearch_server_running_and_enabled(Command,Service):
  # Check that docker service is running and enabled
  docker_service = Service("docker")
  assert docker_service.is_running
  assert docker_service.is_enabled
  # Check that elasticsearch service is running and enabled
  elasticsearch_service = Service("elasticsearch")
  assert elasticsearch_service.is_running
  assert elasticsearch_service.is_enabled

  # Check that elasticsearch-cli ping
  elasticsearch_output = Command.check_output("docker exec elasticsearch elasticsearch-cli ping")
  assert elasticsearch_output == "PONG"

def test_elasticsearch_start_stop(Command,Service):
  Command.run_expect([0],"systemctl stop elasticsearch")
  elasticsearch_service = Service("elasticsearch")
  assert not elasticsearch_service.is_running
  Command.run_expect([0],"systemctl start elasticsearch")
  assert elasticsearch_service.is_running
  Command.run_expect([0],"systemctl restart elasticsearch")
  assert elasticsearch_service.is_running
  elasticsearch_output = Command.check_output("docker exec elasticsearch elasticsearch-cli ping")
  assert elasticsearch_output == "PONG"
