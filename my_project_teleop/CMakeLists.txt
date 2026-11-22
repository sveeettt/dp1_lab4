cmake_minimum_required(VERSION 3.8)
project(my_project_teleop)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

# Установка Python-скриптов
install(PROGRAMS
  scripts/teleop_keyboard
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
