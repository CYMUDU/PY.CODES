{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/CYMUDU/PY.CODES/blob/main/JOYDEEP%20SIR.PY\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pMpuJPRPigRa",
        "outputId": "6838a31d-7945-4a8a-cdba-d13f01f3f346"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "My name is Joydeep\n"
          ]
        }
      ],
      "source": [
        "print(\"My name is Joydeep\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=\"Hello World\"\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "21rO9vL-lvLk",
        "outputId": "57f4c72c-fe87-4f62-c3f2-3580c11b4f12"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello World\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "type(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qTH-g5xzmCG1",
        "outputId": "482648a5-dec6-480b-db91-b8a496d18226"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "str"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Taking input from the users*"
      ],
      "metadata": {
        "id": "d6gMVZwi3a-v"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "c1=input(\"Enter first number: \")\n",
        "c2=input(\"Enter second number: \")\n",
        "z=c1+c2\n",
        "print(z, type(z))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0UsGfwH63ewD",
        "outputId": "11e75e01-15ce-4d85-dc3f-f461caf699de"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter first number: Hello \n",
            "Enter second number: World\n",
            "Hello World <class 'str'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "c1=eval(input(\"Enter first number: \"))\n",
        "c2=eval(input(\"Enter second number: \"))\n",
        "print(c1, type(c1), c2, type(c2))\n",
        "z=c1*c2\n",
        "print(z, type(z))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yu1UFZKw5ED2",
        "outputId": "7960bf6f-b680-47e4-d66c-eb08175a4831"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter first number: 2.5+2.5\n",
            "Enter second number: 4\n",
            "5.0 <class 'float'> 4 <class 'int'>\n",
            "20.0 <class 'float'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Explicit Data type conversion"
      ],
      "metadata": {
        "id": "OyeHJnf66nFK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "i1=int(input(\"Enter first number:\"))\n",
        "i2=int(input(\"ENter second number: \"))\n",
        "print(i1, type(i1), i2, type(i2))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 193
        },
        "id": "WZ5uNQOC6my7",
        "outputId": "467472a0-7fb1-4621-b167-0c314ef6998c"
      },
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter first number:20.5\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "ValueError",
          "evalue": "invalid literal for int() with base 10: '20.5'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipython-input-1607889605.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mi1\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Enter first number:\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mi2\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"ENter second number: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mi1\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtype\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mi1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mi2\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtype\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mi2\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mValueError\u001b[0m: invalid literal for int() with base 10: '20.5'"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "f1=float(input(\"Enter first number:\"))\n",
        "f2=float(input(\"ENter second number: \"))\n",
        "print(f1, type(f1), f2, type(f2))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "n2dzbH-27Yf0",
        "outputId": "6c1171e4-9305-444e-9cb0-a066db8f192d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter first number:20.5\n",
            "ENter second number: 5\n",
            "20.5 <class 'float'> 5.0 <class 'float'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=10.6\n",
        "i3=int(x)\n",
        "print(i3, type(i3))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j5Ph6pA674RU",
        "outputId": "d3767be1-3090-4ab5-b525-b83b8398089a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10 <class 'int'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=\"10.25\"\n",
        "f3=float(x)\n",
        "print(f3, type(f3))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4JGyceCw9Z4Y",
        "outputId": "7b9995b6-1434-4560-807f-d624b2494c66"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10.25 <class 'float'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=\"10.5a\"\n",
        "s3=str(x)\n",
        "print(s3, type(s3))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oRPs3_pZ-RB7",
        "outputId": "ea9b3503-35f1-496d-cf2e-24796b78ebfc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10.5a <class 'str'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "int() can convert from float to integer and string to integer (provided the string contains an integer value)<br>\n",
        "float() can convert from int to float and string to float (provided the string contains a numeric value)<br>\n",
        "str() can convert any data to string"
      ],
      "metadata": {
        "id": "QHTbVdJy91kJ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Assignment*"
      ],
      "metadata": {
        "id": "E2iWhNre-lHo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "x=10\n",
        "y=5\n",
        "x,y,z=2,3,5\n",
        "print(x,y,z)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3HEgg8sj-nlV",
        "outputId": "62de0b24-a642-4ec5-e441-77f3e665464f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2 3 5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x,y=10,5\n",
        "print(\"Before Swapping: \", x,y)\n",
        "x,y=y,x\n",
        "print(\"After Swapping: \",x,y)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "v0_GjP6o_A4U",
        "outputId": "c34e6c57-9cf0-4a5d-c453-5e6de389a215"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Before Swapping:  10 5\n",
            "After Swapping:  5 10\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=5\n",
        "y=7\n",
        "temp=x #temp=5, x=5, y=7\n",
        "x=y #temp=5, x=7, y=7\n",
        "y=temp #temp=5, x=7, y=5\n",
        "print(\"After swapping: \", x,y)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "W5JPiXKN_eQw",
        "outputId": "a74ee93e-ef4a-4736-b320-ab003a9e4e81"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "After swapping:  7 5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Variable names and identifiers*<br>\n",
        "The identifiers are the variables that are used in the program. There are certain rules about how identifiers are formed:<br>\n",
        "Rule 1: Every identifier must begin with a letter (a-z or A-Z) or an underscore ( _ ), which may be followed by any sequence of letters, digits or underscores<br>\n",
        "Rule 2: Identifiers are case sensitive (\"var\" and \"Var\" are 2 different identifiers)<br>\n",
        "Rule 3: Identifiers cannot be reserved words or keywords like True, False, None, and, or, as , assert, break, class, continue, pass, raise etc."
      ],
      "metadata": {
        "id": "XoVo6cUXAsIK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "True=2\n",
        "print(True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        },
        "id": "TFseip1IAxiz",
        "outputId": "142f6b86-44dc-4c88-a155-f77f9cd5e140"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "cannot assign to True (ipython-input-923839229.py, line 1)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"/tmp/ipython-input-923839229.py\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    True=2\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m cannot assign to True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Date: 24.10.2025, Lab Assignments**"
      ],
      "metadata": {
        "id": "CNXsJ74enJWV"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Problem 1*"
      ],
      "metadata": {
        "id": "BxCfcVefn6cl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "name=input(\"Enter your name: \")\n",
        "age=input(\"enter your age: \")\n",
        "print(\"Hello\", name, \"you are\", age, \"years old\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vJCYxZfNnP7t",
        "outputId": "68665f78-8db4-4236-c698-87f39e386c96"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your name: Aman\n",
            "enter your age: 25\n",
            "Hello Aman you are 25 years old\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "name=input(\"Enter your name: \")\n",
        "age=input(\"Enter your age: \")\n",
        "print(f\"Hello {name}, you are {age} years old!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "peTN5ktwn-qq",
        "outputId": "5b957cb4-1e9e-4d86-f640-97a6f7a26546"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your name: Aman\n",
            "Enter your age: 25\n",
            "Hello Aman, you are 25 years old!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Problem 2*"
      ],
      "metadata": {
        "id": "EHkxQHuto6Cu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "num1=int(input(\"Enter 1st number: \"))\n",
        "num2=int(input(\"Enter 2nd number: \"))\n",
        "sum=num1+num2\n",
        "diff=num1-num2\n",
        "prod=num1*num2\n",
        "div=num1/num2\n",
        "print(f\"Sum = {sum}, Difference = {diff}, Product = {prod}, Division = {div:.2f}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nMxEDiPYo8vN",
        "outputId": "3c83ff12-13ab-4206-d743-fb5d443d6a28"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter 1st number: 25\n",
            "Enter 2nd number: 6\n",
            "Sum = 31, Difference = 19, Product = 150, Division = 4.17\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Problem 3*"
      ],
      "metadata": {
        "id": "vwE-XgbqqzKd"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "num1=int(input(\"Enter an integer number: \"))\n",
        "num2=float(input(\"Enter a decimal number: \"))\n",
        "sum=num1+num2\n",
        "print(f\"The sum of {num1} and {num2} is {sum}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MAsg1NLaq1au",
        "outputId": "8891cbc7-557d-4a83-d2c8-467b73da3192"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter an integer number: 10\n",
            "Enter a decimal number: 2.5\n",
            "The sum of 10 and 2.5 is 12.5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Problem 4*"
      ],
      "metadata": {
        "id": "TJ_2S1Dsrj2Y"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "numf=float(input(\"Enter a floating point number: \"))\n",
        "numi=int(numf)\n",
        "nums=str(numf)\n",
        "print(f\"The number in float format is {numf} (type: {type(numf)}), in integer format is {numi} (type: {type(numi)}), and in string format is {nums} (type: {type(nums)})\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_jmrAtQ6rjPP",
        "outputId": "d4cec659-59d9-43f2-83dc-c162161696af"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a floating point number: 28.78\n",
            "The number in float format is 28.78 (type: <class 'float'>), in integer format is 28 (type: <class 'int'>), and in string format is 28.78 (type: <class 'str'>)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Problem 5*"
      ],
      "metadata": {
        "id": "cWdhjuE7tYAU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "x=input(\"Enter 1st number: \")\n",
        "y=input(\"Enter 2nd number: \")\n",
        "print(f\"Before swapping: x = {x}, y = {y}\")\n",
        "x,y=y,x\n",
        "print(f\"After swapping: x = {x}, y = {y}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FyBc1VRVtZ0e",
        "outputId": "b59fa270-9419-4ee1-d6f0-9223aec0d36e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter 1st number: 12\n",
            "Enter 2nd number: 21\n",
            "Before swapping: x = 12, y = 21\n",
            "After swapping: x = 21, y = 12\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Problem 6*"
      ],
      "metadata": {
        "id": "jHlGmYkBuJ7J"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a=eval(input(\"Enter a: \"))\n",
        "b=eval(input(\"Enter b: \"))\n",
        "c=eval(input(\"Enter c: \"))\n",
        "res=(a+b)**2-4*a*c\n",
        "print(f\"The results is {res}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4dBxTmHnuLv9",
        "outputId": "48ee1992-d1c1-44bc-f4ab-f4b9f37024f1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a: 1.0\n",
            "Enter b: 1.0\n",
            "Enter c: 1\n",
            "The results is 0.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Problem 7*"
      ],
      "metadata": {
        "id": "UFjSLnzwvGsT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "num_i=int(input(\"Enter an integer: \"))\n",
        "num_f=float(input(\"Enter a floating number: \"))\n",
        "num_s=input(\"Enter a number: \")\n",
        "num_sf=float(num_s)\n",
        "sum=num_i+num_f+num_sf\n",
        "print(f\"The final sum is {sum} and type is {type(num_sf)}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Rx1ULd8HvItY",
        "outputId": "35702d12-dfbc-43d5-d585-28097e6f8cd3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter an integer: 10\n",
            "Enter a floating number: 10.5\n",
            "Enter a number: 9.5\n",
            "The final sum is 30.0 and type is <class 'float'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Problem 8*"
      ],
      "metadata": {
        "id": "3gfDgrQ4wqFO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "x=eval(input(\"Enter 1st number: \"))\n",
        "y=eval(input(\"Enter 2nd number: \"))\n",
        "result=(x**2+y**2)/(x+y)\n",
        "print(f\"The result is: {result:.3f}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6Nn1srvnwwHC",
        "outputId": "aad9b1a1-9318-4e2f-b1d9-895b93e4e5bf"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter 1st number: 10\n",
            "Enter 2nd number: 2.67\n",
            "The result is: 8.455\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Problem 9*"
      ],
      "metadata": {
        "id": "20xxWTscxbrz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a=b=c=5\n",
        "a=2\n",
        "print(a,b,c)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3I7F5UzmxecO",
        "outputId": "1538bb52-03b2-40b8-a721-a039a29e71b5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2 5 5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Problem 10*"
      ],
      "metadata": {
        "id": "Xs2RHIJzyLLD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "r=eval(input(\"Enter radius of a circle: \"))\n",
        "area=(22/7)*(r**2)\n",
        "circum=2*(22/7)*r\n",
        "print(f\"\\nFor a circle with radius {r}: \\n\\nArea={area:.2f} \\n\\nCircumference={circum:.2f}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AOw5ED-0yM4B",
        "outputId": "5aa7342f-f474-4b6f-c46c-fc25c842ac9f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter radius of a circle: 5\n",
            "\n",
            "For a circle with radius 5: \n",
            "\n",
            "Area=78.57 \n",
            "\n",
            "Circumference=31.43\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Operators and Expressions**"
      ],
      "metadata": {
        "id": "x3WkaT9cjntC"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Basic Operators in python<br>\n",
        "1. Arithmetic Operators<br>\n",
        "2. Comparison Operators <br>\n",
        "3. Logical Operators <br>\n",
        "4. Assignment Operators <br>\n",
        "5. Conditional Operators"
      ],
      "metadata": {
        "id": "gnu4II4Ej0vG"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Arithmetic Operators*"
      ],
      "metadata": {
        "id": "iGQkOGuuliFf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a=10\n",
        "b=3\n",
        "print(a+b)\n",
        "print(a-b)\n",
        "print(a*b)\n",
        "print(a/b) #Division result in float\n",
        "print(a//b) #Quotient in integer\n",
        "print(a%b) #Remainder\n",
        "print(a**b) #10 to the power of 3"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9IUZ0qwklmdy",
        "outputId": "ae8cb278-d6bc-48d6-feba-0cda9ced1918"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "13\n",
            "7\n",
            "30\n",
            "3.3333333333333335\n",
            "3\n",
            "1\n",
            "1000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Comparison Operator*"
      ],
      "metadata": {
        "id": "4jvmf76ZmdPG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a=10\n",
        "b=10\n",
        "print(a==b) #Checks whether the values of the operands are same or not. Returns True if same, False otherwise\n",
        "print(a!=b) #Checks whether the values of the operands are same or not. Returns True if they are not same, False otherwise\n",
        "print(a>b) #Returns True if a>b\n",
        "print(a<b) #Returns True if a<b\n",
        "print(a>=b) #Returns True if a is greater than or equal to b\n",
        "print(a<=b)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0DmgCJe3mmEk",
        "outputId": "5e78dbb2-8234-4cba-a5d3-c770160182ae"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n",
            "False\n",
            "False\n",
            "False\n",
            "True\n",
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Assignment Operator*"
      ],
      "metadata": {
        "id": "ryoqO9YJnxuJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a=10 #Assigns values from right operand/literal to left operand\n",
        "b=3\n",
        "a+=5 # a=a+5 Add and Assign\n",
        "print(a)\n",
        "a-=1 #a=a-1 Subtract and Assign\n",
        "print(a)\n",
        "a*=3 #a=a*3 Multiply and Assign\n",
        "print(a)\n",
        "a/=2 #a=a/2 Division and Assign\n",
        "print(a)\n",
        "a//=2 #a=a//2 Floor division and Assign\n",
        "print(a)\n",
        "a%=4 #a=a%4 Mod and Assign\n",
        "print(a)\n",
        "a**=5 #a=a**5 Exponent and Assign\n",
        "print(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2Hj2yzK1n1kF",
        "outputId": "edf27103-303b-42ba-ff31-cad7472e9ad3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "15\n",
            "14\n",
            "42\n",
            "21.0\n",
            "10.0\n",
            "2.0\n",
            "32.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Bitwise Operators*"
      ],
      "metadata": {
        "id": "OXmj63UepdsO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a=10 #In binary a=1010. Internally integers are represented using 32 bit signed numbers. a=0000 0000 0000 0000 0000 0000 0000 1010\n",
        "b=6 #In binary b=0110. Internally b=0000 0000 0000 0000 0000 0000 0000 0110\n",
        "print(a&b) #Bitwise AND-ing\n",
        "print(a|b) #Bitwise OR-ing\n",
        "print(a^b) #Bitwise XOR-ing\n",
        "print(~a) #Bitwise flip 1111 1111 1111 1111 1111 1111 1111 0101 in 2's complement. In Sign and Magnitude - 0000 0000 0000 0000 0000 0000 0000 1011\n",
        "print(a<<2) #Left shift 2 bits. a=1010. Shifting left by 2 bit produces 101000. Multiplies by 4\n",
        "print(a>>1) #Right shift by 1 bit. Divides by 2"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RdLb6jjCpiX_",
        "outputId": "65fd0e17-8277-4828-f834-86651baecb4f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "14\n",
            "12\n",
            "-11\n",
            "40\n",
            "5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Logical Operator*"
      ],
      "metadata": {
        "id": "SeYk8wuLsMDQ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a=10\n",
        "b=5\n",
        "print((a==10) and (b==4))\n",
        "print((a==10) or (b==4))\n",
        "print(not(a==10))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fFkQHON4sV0W",
        "outputId": "8c892c28-1744-4aaf-da92-dd899b2b388d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n",
            "True\n",
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Membership Operators*"
      ],
      "metadata": {
        "id": "Rdsl7L91tIqy"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a=\"amolfi\"\n",
        "print(\"m\" in a) #Evaluates to True if the element is a member of the set or sequence\n",
        "b=[1,2,3,4,5]\n",
        "print(3 in b)\n",
        "print(\"n\" not in a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YJuILIZQtRTy",
        "outputId": "d7e8be3d-5d2a-4762-bc62-1bd45cdd4629"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n",
            "True\n",
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Suppose an expression contains multiple operators. Like 10+2*5/6+9-7, how will the same be evaluated. Look for operator precedence.<br>\n",
        "Precedence List<br>\n",
        "1. ** <br>\n",
        "2. ~,+,- Unary operators <br>\n",
        "3. *,/,%,// <br>\n",
        "4. +,- <br>\n",
        "5. \\>>, << <br>\n",
        "6. \\& <br>\n",
        "7. \\|,^ <br>\n",
        "8. \\>=,>, <=, < <br>\n",
        "9. == !=<br>\n",
        "10.=, +=,-=,*=,/=, %=,//=, **= <br>\n",
        "11. in, not in <br>\n",
        "12. not, or, and\n"
      ],
      "metadata": {
        "id": "424qXrPgt8Le"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Consider a case where an expression has several operators with same precedence<br>\n",
        "10+3\\*7\\/2\\%3\\//2+3-2\\*2\\/3<br>\n",
        "In this case what would be the sequence of the operations?<br>\n",
        "In these cases we need to look at the associativity of the operators"
      ],
      "metadata": {
        "id": "s0R4LQMi6WYF"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "In case several operators have the same precedence, the associativity of the operators will determine the order in which the operators will be executed<br>\n",
        "In an expression like 3\\*2\\/4, where \\* and \\/ both have the same precedence, the order of execution will be determined by the associativity of \\* and \\/. The associativity in this case is left to right, i.e., the left operator will be executed first. <br>\n",
        "Example of left to right associativity<br>\n",
        "\\+, \\-, \\*, \\/<br>\n",
        "Example of right to left associativity<br>\n",
        "**, Unary operators"
      ],
      "metadata": {
        "id": "nVMa0SQz6_Mj"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Few Examples:"
      ],
      "metadata": {
        "id": "pic9p3E78HSY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "x=10+3*2\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "huJJBt1C6V4S",
        "outputId": "497d133f-19da-48a4-eacb-66364facf5ac"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "16\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=(10+3)*2\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "z0DlZeI48YOv",
        "outputId": "e75baf2d-079c-469d-8a47-9ac07a4e4506"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "26\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=2**3**2\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tgmHfDgi8dm3",
        "outputId": "17cbb969-4e2f-49fd-e788-da55b1fb9a5d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "512\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=-2**2\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "obCdU9Ku82dS",
        "outputId": "4e8a5b0a-1dfb-41d2-e055-29fb991fd703"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "-4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=3+2>4*1\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RMD-NP9q9MkS",
        "outputId": "0a507fac-b7cd-45c7-a880-798d59a8d380"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=(3+2>4 and 5-1 == 3 or 2+2 ==5) #(5>4 and 4==3 or 4 == 5 ) --> (True and False or False) --> False\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5tMZuYRy9jAL",
        "outputId": "a4dafe3b-3732-4ab9-fb91-2b4593bf6a2c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "UuLrcMjtxHR9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "x = (3<2<8) #(3<5) and (5<8)\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uv1gfNwZAFKs",
        "outputId": "a98ce020-70cf-4cd5-ecf2-06845e530e32"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=5 & 3 == 1 # 0101 & 0011 == 1 --> 0001 == 1 --> 1 == 1 --> True\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MOIMmJjrBEEN",
        "outputId": "298d398d-7055-42a7-c870-ff67260b37e5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=2\n",
        "y=3\n",
        "z=(x+y)*(x**y)/(y-x)\n",
        "print(z)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vhffNIGiCjEF",
        "outputId": "16bc8ba8-5d2f-4849-a54a-70301f423773"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "40.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Functions**"
      ],
      "metadata": {
        "id": "RL162OXkDWzJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def Hello():\n",
        "  print(\"Hello World\")\n",
        "  print(\"Hello World again\")\n",
        "Hello()\n",
        "print(\"Outside Function\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dYn_c0CuDZTM",
        "outputId": "a082caf6-d217-4ae6-b846-dd03f88389d1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello World\n",
            "Hello World again\n",
            "Outside Function\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def printName(person):\n",
        "  print(\"Hello \" + person)"
      ],
      "metadata": {
        "id": "Z19fsJ-kEk2S"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "printName(\"Aman\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "T9OOomiFDotP",
        "outputId": "e296af8c-da0e-49e1-e402-6cea404ac78e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello Aman\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def findSum(num1, num2=10):\n",
        "  print(f\"The sum of {num1} and {num2} is {num1+num2}\")"
      ],
      "metadata": {
        "id": "fEp9uY8vFGye"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "a=5\n",
        "b=7\n",
        "findSum(a,b)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lmuhYxJPFUbJ",
        "outputId": "bfce2dd7-322a-4394-f6c9-e3eab07c1de7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The sum of 5 and 7 is 12\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "94esuZgzFvRa"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "a=10\n",
        "b=5\n",
        "print(b<<1)\n",
        "print(a&b)\n",
        "print(a|b)\n",
        "print(~b)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LX3jXcLAd7x9",
        "outputId": "c997cfb1-cd9f-4bc0-f8d1-50155b663f38"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10\n",
            "0\n",
            "15\n",
            "-6\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Write a function to check whether a triangle given its sides is a right angled triangle\n",
        "\n",
        "The function name should be checkRightTriangle, to which the length of the sides should be passed as paramter from the calling function. In the parameter list, the length of the longest side should be passed as the first argument."
      ],
      "metadata": {
        "id": "YhyMZb4me-AO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def checkRightTriangle(l,a,b):\n",
        "  p = l**2==a**2+b**2\n",
        "  if p==True:\n",
        "    print(\"Right Angled\")\n",
        "  else:\n",
        "    print(\"Not Right Angled\")"
      ],
      "metadata": {
        "id": "vNDW9xzzjWNR"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def main():\n",
        "  l=eval(input(\"Enter the longest side: \"))\n",
        "  a=eval(input(\"Enter the second side: \"))\n",
        "  b=eval(input(\"Enter the third side: \"))\n",
        "  checkRightTriangle(l,a,b)\n",
        "main()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uTNLSPxbkCJF",
        "outputId": "11097d4d-cb3b-4c91-dab0-687ed843349e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the longest side: 7\n",
            "Enter the second side: 4\n",
            "Enter the third side: 5\n",
            "Not Right Angled\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Few Exercises"
      ],
      "metadata": {
        "id": "t2G8dDO7k25t"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def f(x):\n",
        "  return x**2\n",
        "\n",
        "def g(x):\n",
        "  return x+2\n",
        "\n",
        "def h(x):\n",
        "  return f(g(x))\n",
        "\n",
        "print(h(3))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4-gK3ldNk5MS",
        "outputId": "179a6f4d-85fc-4e4a-f8d2-e34081bf2119"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "25\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def f(a):\n",
        "  return a**2\n",
        "\n",
        "def g(a):\n",
        "  return f(a) + f(a+1)\n",
        "\n",
        "print(g(2))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xCxx9LnVlkOw",
        "outputId": "59cd007a-c135-4637-bdb3-f69942fd8803"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "13\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def f(a):\n",
        "  return a+2\n",
        "\n",
        "def g(a):\n",
        "  return a*2\n",
        "\n",
        "def h(a):\n",
        "  return f(g(a))+g(f(a))\n",
        "\n",
        "print(h(2))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ffnjb6-SmIU1",
        "outputId": "e08d9bef-ff52-4746-a83e-51c381387f8e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "14\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "5y7VmKvEgHkZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "z = 5>3 == 3<4\n",
        "print(z)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eHHwvmFWm5ii",
        "outputId": "6bc18eb0-2598-40bb-c1f5-6c8fe0e2b517"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "z = 3**2*2**3\n",
        "print(z)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rxmj2r9ZnUoR",
        "outputId": "3cbf4238-7a9e-43ef-b046-91a046d9f013"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "72\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "z = 4**2**1\n",
        "print(z)"
      ],
      "metadata": {
        "id": "UvDBGMqCnqo2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Python Assignment 1**"
      ],
      "metadata": {
        "id": "b_o7OqpYxzc1"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "P1"
      ],
      "metadata": {
        "id": "v5DyczJEzgw5"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def mathOperation(n1, n2):\n",
        "  print(f\"The sum of {n1} and {n2} is {n1+n2}\")\n",
        "  print(f\"The multiplication of {n1} and {n2} is {n1*n2}\")\n",
        "  print(f\"The division result of {n1} and {n2} is {n1/n2}\")\n",
        "  print(f\"The quotient of dividing {n1} and {n2} is {n1//n2}\")\n",
        "  print(f\"The remainder of diding {n1} by {n2} is {n1%n2}\")\n",
        "\n",
        "\n",
        "def main():\n",
        "  num1=int(input(\"Enter 1st integer: \"))\n",
        "  num2=int(input(\"Enter 2nd integer: \"))\n",
        "  mathOperation(num1, num2)\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bjYbo3Q0yBLC",
        "outputId": "2a665d41-c492-4b66-b4ef-8f11b52692b6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter 1st integer: 16\n",
            "Enter 2nd integer: 3\n",
            "The sum of 16 and 3 is 19\n",
            "The multiplication of 16 and 3 is 48\n",
            "The division result of 16 and 3 is 5.333333333333333\n",
            "The quotient of dividing 16 and 3 is 5\n",
            "The remainder of diding 16 by 3 is 1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "P2"
      ],
      "metadata": {
        "id": "AA34RP9jzjZc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def findMissing(avg, n1, n2):\n",
        "  z= (3*avg)-(n1+n2)\n",
        "  print(f\"The missing number is {z}\")\n",
        "\n",
        "def main():\n",
        "  num1=eval(input(\"Enter 1st number: \"))\n",
        "  num2=eval(input(\"Enter 2nd number: \"))\n",
        "  avg=eval(input(\"Enter average: \"))\n",
        "  findMissing(avg, num1, num2)\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "g8rwz34SzkHh",
        "outputId": "86259191-2740-4d1c-de69-6a6e76a1c5dc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter 1st number: 3\n",
            "Enter 2nd number: 5\n",
            "Enter average: 10\n",
            "The missing number is 22\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "P3"
      ],
      "metadata": {
        "id": "ZHUVDHQT0eWk"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def timeConvert(tm):\n",
        "  hrs=tm//60\n",
        "  mins=tm%60\n",
        "  print(f\"{tm} minutes is {hrs} hours and {mins} minutes\")\n",
        "\n",
        "def main():\n",
        "  tim=int(input(\"Enter time in minutes: \"))\n",
        "  timeConvert(tim)\n",
        "\n",
        "main()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oT4ao6z3xypO",
        "outputId": "d82815af-4353-4df1-bb18-279291cce592"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter time in minutes: 75\n",
            "75 minutes is 1 hours and 15 minutes\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "P4"
      ],
      "metadata": {
        "id": "YD3gBbIg13hA"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def findAreaPeri(r):\n",
        "  area=(22/7)*r**2\n",
        "  circum=2*(22/7)*r\n",
        "  print(f\"The area of the circle is {area:.2f} and circumference is {circum:.2f}\")\n",
        "\n",
        "def main():\n",
        "  rad=eval(input(\"Enter radius: \"))\n",
        "  findAreaPeri(rad)\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zB1WdGGO14q9",
        "outputId": "bbdb67e9-eabe-4d6c-8753-c559d121d815"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter radius: 5\n",
            "The area of the circle is 78.57 and circumference is 31.43\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "P5"
      ],
      "metadata": {
        "id": "HLtqWuQe2-ah"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def findDistance(t,a,u):\n",
        "  s=(u*t)+(0.5*a*t**2)\n",
        "  print(f\"The distance travelled by the body is {s}\")\n",
        "\n",
        "def main():\n",
        "  u=eval(input(\"Enter initial velocity: \"))\n",
        "  a=eval(input(\"Enter acceleration: \"))\n",
        "  t=eval(input(\"Enter time of travel: \"))\n",
        "  findDistance(t,a,u)\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_baIxi0z2_tt",
        "outputId": "e2428e8a-80b8-4453-fe59-c922cb5cfccd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter initial velocity: 5\n",
            "Enter acceleration: 9.8\n",
            "Enter time of travel: 6\n",
            "The distance travelled by the body is 206.4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "P6"
      ],
      "metadata": {
        "id": "3GWshdva4Jxa"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def centToFahr(c):\n",
        "  fahr=c*9/5+32\n",
        "  print(f\"Temperature {c} degree celsius is {fahr} degree fahrenheit\")\n",
        "\n",
        "def main():\n",
        "  cel=eval(input(\"Enter degree in celsius: \"))\n",
        "  centToFahr(cel)\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dTwxoYmj4Kyo",
        "outputId": "de37d364-9adc-405c-fe86-8bc4cb9043ff"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter degree in celsius: 5\n",
            "Temperature 5 degree celsius is 41.0 degree fahrenheit\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Local variables and Global variables*"
      ],
      "metadata": {
        "id": "lmRfBXZ5cCL6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def func1(x,y): #Formal arguments, local variables scope only within the function body\n",
        "  z=4 #local variable\n",
        "  print(x,y,z)\n",
        "\n",
        "func1(1,2)\n",
        "print(x,y,z)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 193
        },
        "id": "n8x_2Bs5cIQ8",
        "outputId": "2d454c41-e3ba-49b6-b89e-0aa73ae2cb12"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 4\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "name 'x' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipython-input-545960733.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0mfunc1\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0my\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mz\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m: name 'x' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=100  #Global variable\n",
        "def func2():\n",
        "  print(x)\n",
        "\n",
        "func2()\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ygp-9yTndwNA",
        "outputId": "ee2a4244-8697-45c0-a73b-13b8ac4b6daa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "100\n",
            "100\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=100\n",
        "def func3():\n",
        "  x=20\n",
        "  print(x)\n",
        "\n",
        "func3()\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m9EZFfyPeYBW",
        "outputId": "1061b7fd-710f-4001-ecc4-f0ae468f8688"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "20\n",
            "100\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=100\n",
        "def func4(x):\n",
        "  print(x)\n",
        "\n",
        "func4(20)\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "22YSnazsfxiF",
        "outputId": "cbc8c879-ca98-4868-ed9e-1e0b5b1c8739"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "20\n",
            "100\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=100\n",
        "def func5():\n",
        "  global x\n",
        "  x=20\n",
        "  print(x)\n",
        "\n",
        "func5()\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FnGM693EgIuK",
        "outputId": "ac46ad23-28e4-4eda-a428-df7e5b508afb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "20\n",
            "20\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Returning values from a function*"
      ],
      "metadata": {
        "id": "bnoi3s5Pgsyr"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def findAreaRect(len, br):\n",
        "  area = len*br\n",
        "  return area\n",
        "\n",
        "def main():\n",
        "  l=eval(input(\"Enter length: \"))\n",
        "  b=eval(input(\"Enter breadth:\"))\n",
        "  a = findAreaRect(l,b)\n",
        "  print(f\"The area of rectangle is {a}\")\n",
        "\n",
        "main()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OJHQtF1XgqWS",
        "outputId": "ba37b85d-0c95-470c-dd2b-f95635c72bda"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter length: 10\n",
            "Enter breadth:5\n",
            "The area of rectangle is 50\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Write a function that takes as arguments the principal amount, rate of interest per annum in percentage and the time duration. It returns the simple interest accumulated, which is printed the main funtcion*"
      ],
      "metadata": {
        "id": "BB2Vt9Cfh5xz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def findSimpleInter(a, r, t):\n",
        "  inter=a*r*t/100\n",
        "  return inter\n",
        "\n",
        "def main():\n",
        "  amt=eval(input(\"Enter principal amount: \"))\n",
        "  rate=eval(input(\"Enter rate of interest per annum in percentage: \"))\n",
        "  time=eval(input(\"Enter time duration: \"))\n",
        "  interest = findSimpleInter(amt,rate, time) #Actual arguments\n",
        "  print(f\"The interest accumulated is {interest}\")\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qni0BOZ6iM2v",
        "outputId": "94adfdc6-2137-42c1-ee67-e29b6005681c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter principal amount: 1000\n",
            "Enter rate of interest per annum in percentage: 12\n",
            "Enter time duration: 2\n",
            "The interest accumulated is 240.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Pass by value*"
      ],
      "metadata": {
        "id": "L89xg4jWknaj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def func6(x):\n",
        "  x+=1\n",
        "\n",
        "x=1\n",
        "x=func6(x)\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YrDYd2fxjdUz",
        "outputId": "8ffc643e-ad27-47f2-f31e-89c45378b674"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "None\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def func6_mod(x):\n",
        "  x+=1\n",
        "  return x\n",
        "\n",
        "x=1\n",
        "x=func6_mod(x)\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PbPsIHapkNeu",
        "outputId": "5a7e6210-116f-4adf-aa10-3458004e42d4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Math Library*"
      ],
      "metadata": {
        "id": "UXWMcc5fmN5R"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "t=math.sqrt(2)\n",
        "print(t)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "10R1JurymNTf",
        "outputId": "8a88af09-fa72-429d-a079-5244a13c6733"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1.4142135623730951\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "sqrt(x), sin(x), cos(x), tan(x), asin(x), acos(x), atan(x), log(x), log10(x), exp(x), ceil(x), floor(x), pi, e"
      ],
      "metadata": {
        "id": "4gRwRzIhmZ1m"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Decision Structure**"
      ],
      "metadata": {
        "id": "Ja8N5JPFmzWm"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Write a function that converts from celsius to fahrenheit, and the function prints \"Temperature Too High\" if the fahrenheit value is greater than 100. If its is lesser than 40, print, \"Temperature too cold\""
      ],
      "metadata": {
        "id": "UNc5dQALnTKw"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def celToFahr(c):\n",
        "  f=(9/5)*c+32\n",
        "  if f>100:\n",
        "    print(\"Temperature Too High\")\n",
        "  if f<40:\n",
        "    print(\"Temperature too cold\")\n",
        "\n",
        "c=50\n",
        "celToFahr(c)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yEL6-XHFnRd5",
        "outputId": "405c3e3d-8bff-4d6f-cc16-8f0439251a94"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Temperature Too High\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*One way decision*"
      ],
      "metadata": {
        "id": "PzyT_1vC9srh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Statements before if\n",
        "if <condition>:\n",
        "  #Statements within if\n",
        "#Statements after if"
      ],
      "metadata": {
        "id": "OaMX8WFT9DNV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Two way decision*"
      ],
      "metadata": {
        "id": "h66suUxj98op"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Suppose we are given coefficients a,b, and c of a quadratic equation. We need to determine whether the roots are complex or not. If the roots are complex, then simply print that roots are complex. Otherwise print the roots of the equation."
      ],
      "metadata": {
        "id": "CadESwQ_-LIu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def findRoots(a,b,c):\n",
        "  D=b**2-4*a*c\n",
        "  if D<0:\n",
        "    print(\"Roots are complex\")\n",
        "  else:\n",
        "    r1=(-b+D**0.5)/(2*a)\n",
        "    r2=(-b-D**0.5)/(2*a)\n",
        "    print(f\"The roots of the QE are {r1} and {r2}\")\n",
        "\n",
        "def main():\n",
        "  a=eval(input(\"Enter coefficient a: \"))\n",
        "  b=eval(input(\"Enter coefficient b: \"))\n",
        "  c=eval(input(\"Enter coefficient c: \"))\n",
        "  findRoots(a,b,c)\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mOtNZfhJ-hQN",
        "outputId": "f2816130-2d39-4937-8770-5b8191295111"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter coefficient a: 4\n",
            "Enter coefficient b: 4\n",
            "Enter coefficient c: 1\n",
            "The roots of the QE are -0.5 and -0.5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Print the roots of the Quadratic equation. if D\\< 0, the print, Roots are complex. However, if D==0, print Only one root. If D\\> 0, print both the roots"
      ],
      "metadata": {
        "id": "2XjgtCZCAR-D"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Multiway decisions*"
      ],
      "metadata": {
        "id": "PbRU5YTCAtJG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def findRoots_1(a,b,c):\n",
        "  D=b**2-4*a*c\n",
        "  if D<0:\n",
        "    print(\"Roots are complex\")\n",
        "  elif D==0:\n",
        "    r=-b/(2*a)\n",
        "    print(f\"Only one root {r:.2f}\")\n",
        "  else:\n",
        "    r1=(-b+D**0.5)/(2*a)\n",
        "    r2=(-b-D**0.5)/(2*a)\n",
        "    print(f\"The roots of the QE are {r1:.2f} and {r2:.2f}\")\n",
        "\n",
        "def main():\n",
        "  a=eval(input(\"Enter the value of a: \"))\n",
        "  b=eval(input(\"Enter the value of b: \"))\n",
        "  c=eval(input(\"Enter the value of c: \"))\n",
        "  findRoots_1(a,b,c)\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uxTU7nBRAx3A",
        "outputId": "b6dc6cb7-6f19-478c-d694-5c318d4b96d9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the value of a: 2\n",
            "Enter the value of b: 4\n",
            "Enter the value of c: 1\n",
            "The roots of the QE are -0.29 and -1.71\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Suppose you want to find the maximum of 3 numbers. Write a function that does so. Do not use any math library functions."
      ],
      "metadata": {
        "id": "baexJ57PCm4u"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def findMax(a,b,c):\n",
        "  if a>b and a>c:\n",
        "    print(f\"{a} is largest\")\n",
        "  elif b>a and b>c:\n",
        "    print(f\"{b} is largest\")\n",
        "  else:\n",
        "    print(f\"{c} is largest\")\n",
        "\n",
        "def main():\n",
        "  num1=eval(input(\"Enter 1st number: \"))\n",
        "  num2=eval(input(\"Enter 2nd number: \"))\n",
        "  num3=eval(input(\"Enter 3rd number: \"))\n",
        "  findMax(num1, num2, num3)\n",
        "\n",
        "main()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1tXjJ6KsDDIk",
        "outputId": "6a30f7fc-6034-4537-830e-6012bda94b32"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter 1st number: 2\n",
            "Enter 2nd number: 7\n",
            "Enter 3rd number: 10\n",
            "10 is largest\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def findMax_Nested(a,b,c):\n",
        "  if a>b:\n",
        "    if a>c:\n",
        "      print(f\"{a} is largest\")\n",
        "    else:\n",
        "      print(f\"{c} is largest\")\n",
        "  else:\n",
        "    if b>c:\n",
        "      print(f\"{b} is largest\")\n",
        "    else:\n",
        "      print(f\"{c} is largest\")\n",
        "\n",
        "def main():\n",
        "  num1=eval(input(\"Enter 1st number: \"))\n",
        "  num2=eval(input(\"Enter 2nd number: \"))\n",
        "  num3=eval(input(\"Enter 3rd number: \"))\n",
        "  findMax_Nested(num1, num2, num3)\n",
        "\n",
        "main()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cHQHyW0lEADV",
        "outputId": "dc2edc31-bf5d-467b-908e-3df60de74029"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter 1st number: 10\n",
            "Enter 2nd number: 2\n",
            "Enter 3rd number: 1\n",
            "10 is largest\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Write a program that tests whether a triangle is scalene, isoceles or equilateral, given its sides*"
      ],
      "metadata": {
        "id": "B1n20yYTFV3k"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def triangleType(a,b,c):\n",
        "  if a==b==c:\n",
        "    print(\"Triangle is equilateral\")\n",
        "  elif (a!=b) and (a!=c) and (b!=c):\n",
        "    print(\"Triangle is scalene\")\n",
        "  else:\n",
        "    print(\"Triangle is isoceles\")\n",
        "\n",
        "def main():\n",
        "  a=eval(input(\"Enter side a: \"))\n",
        "  b=eval(input(\"Enter side b: \"))\n",
        "  c=eval(input(\"Enter side c: \"))\n",
        "  triangleType(a,b,c)\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rWn9zX0JGxBI",
        "outputId": "7f22e5bf-6ac9-4566-9436-d5b3b541d35e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter side a: 5\n",
            "Enter side b: 5\n",
            "Enter side c: 5\n",
            "Triangle is equilateral\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "Side1=int(input(\"Enter the length of the first side: \"))\n",
        "Side2=int(input(\"Enter the length of the second side: \"))\n",
        "Side3=int(input(\"Enter the length of the third side: \"))\n",
        "if Side1==Side2==Side3:\n",
        "  print(\"The triangle is equilateral\")\n",
        "elif Side1==Side2 or Side1==Side3 or Side2==Side3:\n",
        "  print(\"The triangle is isosceles\")\n",
        "else:\n",
        "  print(\"The triangle is scalene\")"
      ],
      "metadata": {
        "id": "BS3ZEKVhH1IJ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Tutorial Sheet Problems 7.11.2025**"
      ],
      "metadata": {
        "id": "8bE23iEkfTRq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def isPositive(x):\n",
        "  if x>=0:\n",
        "    print(f\"{x} is positive\")\n",
        "    return\n",
        "  print(f\"{x} is negative\")\n",
        "\n",
        "def main():\n",
        "  x=eval(input(\"Enter x: \"))\n",
        "  isPositive(x)\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RSXIAofSfY2q",
        "outputId": "a4c505f1-7d15-406f-aa58-cc4ba482bd49"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter x: -22\n",
            "-22 is negative\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def checkEven(x):\n",
        "  if x%2==0:\n",
        "    print(f\"{x} is even\")\n",
        "  else:\n",
        "    print(f\"{x} is odd\")\n",
        "\n",
        "def main():\n",
        "  x=int(input(\"Enter integer x: \"))\n",
        "  checkEven(x)\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ja1lxvnJgLvB",
        "outputId": "34e42bcd-40d3-4b77-89b8-c09a11f0c790"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter integer x: 34\n",
            "34 is even\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def checkAge(x):\n",
        "  if x>=18:\n",
        "    print(\"Adult\")\n",
        "  else:\n",
        "    print(\"Minor\")\n",
        "\n",
        "def main():\n",
        "  age=int(input(\"Enter age: \"))\n",
        "  checkAge(age)\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wj1dZuWLgtya",
        "outputId": "6a2f4841-9fc9-4850-95cf-682e52099fad"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter age: 12\n",
            "Minor\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def checkTemp(t):\n",
        "  if t>30:\n",
        "    print(\"Hot day\")\n",
        "  else:\n",
        "    print(\"Pleasant day\")\n",
        "\n",
        "def main():\n",
        "  temp=int(input(\"Enter the temperature: \"))\n",
        "  checkTemp(temp)\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RXM-ECeuhQfp",
        "outputId": "db99af5a-33c6-4835-df92-4b135e55cbc0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the temperature: 32\n",
            "Hot day\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def checkVowel(v):\n",
        "  if v=='a' or v=='e' or v=='i' or v=='o' or v=='u':\n",
        "    print(f\"{v} is a vowel\")\n",
        "  else:\n",
        "    print(f\"{v} is a consonant\")\n",
        "\n",
        "def main():\n",
        "  v=input(\"Enter a character: \")\n",
        "  checkVowel(v)\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ou01fRoghxZJ",
        "outputId": "bf994a69-307f-4e61-ef61-45928f770df6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a character: i\n",
            "i is a vowel\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def checkDiv(x):\n",
        "  if x%5==0:\n",
        "    print(f\"{x} is divisible by 5\")\n",
        "  else:\n",
        "    print(f\"{x} is not divisible by 5\")\n",
        "\n",
        "def main():\n",
        "  inp=int(input(\"Enter a number: \"))\n",
        "  checkDiv(inp)\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vpAUznJ_iZ7E",
        "outputId": "2801966e-c0c1-482d-99fa-b133c3762dd9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 65\n",
            "65 is divisible by 5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def checkGreater(x,y):\n",
        "  if x>y:\n",
        "    print(f\"{x} is greater\")\n",
        "  else:\n",
        "    print(f\"{y} is greater\")\n",
        "\n",
        "def main():\n",
        "  x=int(input(\"Enter first number: \"))\n",
        "  y=int(input(\"Enter second number: \"))\n",
        "  checkGreater(x,y)\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dhs-QdY6jAnd",
        "outputId": "9eaa501e-86f0-4132-f2a4-a3cce3c95725"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter first number: 12\n",
            "Enter second number: 19\n",
            "19 is greater\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Problem 16"
      ],
      "metadata": {
        "id": "8YWw8-Zjmr3l"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def main():\n",
        "  inp=int(input(\"Enter marks: \"))\n",
        "  if inp>=90:\n",
        "    print(\"Excellent\")\n",
        "  elif 70<inp<=89:\n",
        "    print(\"Good\")\n",
        "  elif 50<inp<=70:\n",
        "    print(\"Average\")\n",
        "  else:\n",
        "    print(\"Fail\")\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lx5RYenrjlvr",
        "outputId": "bd4822cc-0378-4eaa-9a14-c2db8073152e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter marks: 70\n",
            "Average\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def main():\n",
        "  x=int(input(\"Enter a number: \"))\n",
        "  if x>0:\n",
        "    print(\"Positive\")\n",
        "  elif x==0:\n",
        "    print(\"Zero\")\n",
        "  else:\n",
        "    print(\"Negative\")\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QA0NCg5ym1Ls",
        "outputId": "47761b19-c82d-41cb-c466-44e203760afa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: -9\n",
            "Negative\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def main():\n",
        "  day=int(input(\"Enter week day (1-7): \"))\n",
        "  match day:\n",
        "    case 1: print(\"Monday\")\n",
        "    case 2: print(\"Tuesday\")\n",
        "    case 3: print(\"Wednesday\")\n",
        "    case 4: print(\"Thursday\")\n",
        "    case 5: print(\"Friday\")\n",
        "    case 6: print(\"Saturday\")\n",
        "    case 7: print(\"Sunday\")\n",
        "    case _: print(\"Invalid input\")\n",
        "\n",
        "main()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hM2tJVUcoYOX",
        "outputId": "772e55a4-6b9c-4b5e-86cc-1f71d405deed"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter week day (1-7): 12\n",
            "Invalid input\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Problem 28"
      ],
      "metadata": {
        "id": "zYwKuUx6qGBy"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def main():\n",
        "  x=int(input(\"Enter an integer: \"))\n",
        "  if x<0:\n",
        "    print(\"Input Positive Number Only\")\n",
        "  elif x<10:\n",
        "    print(\"Single digit\")\n",
        "  elif x<100:\n",
        "    print(\"Double digit\")\n",
        "  elif x<1000:\n",
        "    print(\"Three digits\")\n",
        "  else:\n",
        "    print(\"More than three digits\")\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "T-ptlaq7pRcN",
        "outputId": "31bc1129-28bb-43e4-f2c6-0aad32ade0ec"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter an integer: 8888\n",
            "More than three digits\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def main():\n",
        "  x=float(input(\"Enter a number: \"))\n",
        "  if x.is_integer():\n",
        "    print(f\"{x} is integer\")\n",
        "  else:\n",
        "    print(f\"{x} is float\")\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JlGAlhRdsCoA",
        "outputId": "7525a635-2c7b-4839-da75-05c990e75493"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 23.0\n",
            "23.0 is integer\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Assignment 2 Date: 07.11.2025**"
      ],
      "metadata": {
        "id": "HLn4cFlH8hWK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def findRoots():\n",
        "  a=eval(input(\"Enter coefficient a: \"))\n",
        "  b=eval(input(\"Enter coefficient b: \"))\n",
        "  c=eval(input(\"Enter coefficient c: \"))\n",
        "  D=b**2-4*a*c\n",
        "\n",
        "  if D>0:\n",
        "    r1=(-b+D**0.5)/(2*a)\n",
        "    r2=(-b-D**0.5)/(2*a)\n",
        "    print(f\"The roots of the QE are real and are {r1:.2f} and {r2:.2f}\")\n",
        "\n",
        "  elif D==0:\n",
        "    r=(-b)/(2*a)\n",
        "    print(f\"The root of the QE is {r:.2f}\")\n",
        "\n",
        "  else:\n",
        "    re=(-b)/(2*a)\n",
        "    imag=(-D)**0.5/(2*a)\n",
        "    print(f\"The roots of the QE are impaginary and are {re:.2f}+{imag:.2f}i and {re:.2f}-{imag:.2f}i\")\n",
        "\n",
        "findRoots()\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dFx9p3qI8mvB",
        "outputId": "fbd7217b-70e1-419c-b65c-c1169f481de5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter coefficient a: 5\n",
            "Enter coefficient b: 1\n",
            "Enter coefficient c: 5\n",
            "The roots of the QE are impaginary and are -0.10+0.99i and -0.10-0.99i\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "def findIntersect():\n",
        "  x1=eval(input(\"Enter x coord of center of 1st circle: \"))\n",
        "  y1=eval(input(\"Enter y coord of center of 1st circle: \"))\n",
        "  r1=eval(input(\"Enter radius of 1st circle: \"))\n",
        "\n",
        "  x2=eval(input(\"Enter x coord of center of 2nd circle: \"))\n",
        "  y2=eval(input(\"Enter y coord of center of 2nd circle: \"))\n",
        "  r2=eval(input(\"Enter radius of 2nd circle: \"))\n",
        "\n",
        "  dist=math.sqrt((x2-x1)**2+(y2-y1)**2)\n",
        "  if dist<r1+r2:\n",
        "    print(\"Intersect\")\n",
        "  elif dist==r1+r2:\n",
        "    print(\"Touching\")\n",
        "  else:\n",
        "    print(\"Separate\")\n",
        "\n",
        "findIntersect()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9ZQ8lnXD_tFk",
        "outputId": "eb9173ed-5ea2-44af-cca9-4b1fc3e175aa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter x coord of center of 1st circle: 0\n",
            "Enter y coord of center of 1st circle: 0\n",
            "Enter radius of 1st circle: 5\n",
            "Enter x coord of center of 2nd circle: 8\n",
            "Enter y coord of center of 2nd circle: 0\n",
            "Enter radius of 2nd circle: 3\n",
            "Touching\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "def findMaxHeight():\n",
        "  u=eval(input(\"Enter initial velocity: \"))\n",
        "  th_d=eval(input(\"Enter angle of projection: \"))\n",
        "  th=math.radians(th_d)\n",
        "  g=9.8\n",
        "  ht=(u**2*(math.sin(th))**2)/(2*g)\n",
        "  print(f\"The maximum height reached is {ht:.2f}\")\n",
        "\n",
        "findMaxHeight()\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4JrAxIT1AGvW",
        "outputId": "b7c36235-e6fb-473a-bf2c-727d386ae827"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter initial velocity: 20\n",
            "Enter angle of projection: 45\n",
            "The maximum height reached is 10.20\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def findComplexDiv():\n",
        "  a=eval(input(\"Enter real part of 1st complex number: \"))\n",
        "  b=eval(input(\"Enter imag part of 1sty complex number: \"))\n",
        "  c=eval(input(\"Enter real part of 2nd complex number: \"))\n",
        "  d=eval(input(\"Enter imag part of 2nd complex number: \"))\n",
        "  re=(a*c+b*d)/(c**2-d**2)\n",
        "  imag=(b*c-a*d)/(c**2-d**2)\n",
        "  print(f\"The division result is {re:.2f}+{imag:.2f}i\")\n",
        "\n",
        "findComplexDiv()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "J1ZdkNbXC2ul",
        "outputId": "b6946536-c6be-4f11-d698-76da4be5e04d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter real part of 1st complex number: 4\n",
            "Enter imag part of 1sty complex number: 2\n",
            "Enter real part of 2nd complex number: 3\n",
            "Enter imag part of 2nd complex number: -1\n",
            "The division result is 1.25+1.25i\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def checkLeapYear():\n",
        "  y=int(input(\"Enter year: \"))\n",
        "  if y%4==0:\n",
        "    if y%100!=0:\n",
        "      print(\"Leap year\")\n",
        "    else:\n",
        "      if y%400==0:\n",
        "        print(\"Leap year\")\n",
        "      else:\n",
        "        print(\"Not a leap year\")\n",
        "  else:\n",
        "    print(\"Not a leap year\")\n",
        "\n",
        "checkLeapYear()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yrXVryHzEY5T",
        "outputId": "418db7e8-5f02-449e-d758-dbb037167eb9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter year: 2000\n",
            "Leap year\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Loops**"
      ],
      "metadata": {
        "id": "gUnbuXVvWTJy"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Input 2 numbers and find their sum"
      ],
      "metadata": {
        "id": "tZMNwaiqWc_b"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "n1=eval(input(\"Enter a number: \"))\n",
        "n2=eval(input(\"Enter a number: \"))\n",
        "sum=n1+n2\n",
        "print(sum)"
      ],
      "metadata": {
        "id": "RBqa8fTpWf-0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Input 5 numbers and find their sum"
      ],
      "metadata": {
        "id": "dZV9C817XHUN"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Initialize sum to 0<br>\n",
        "Loop 5 times<br>\n",
        "$\\quad$ Enter a number<br>\n",
        "$\\quad$ Add the number to sum<br>\n",
        "Print sum"
      ],
      "metadata": {
        "id": "OBXxBAHFXOMH"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def findSum():\n",
        "  sum=0\n",
        "  for i in range(5):\n",
        "    x=eval(input(\"Enter a number: \"))\n",
        "    sum+=x #sum=sum+x\n",
        "  print(f\"The sum of the numbers is {sum}\")\n",
        "\n",
        "findSum()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "W1_4Hd4yYWW_",
        "outputId": "fdd6b0af-4ffd-4a62-a404-22616d5d2b94"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 2\n",
            "Enter a number: 1\n",
            "Enter a number: 4\n",
            "Enter a number: 3\n",
            "Enter a number: 5\n",
            "The sum of the numbers is 15\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Find the sum of the first n natural numbers, where n is given as input by the user"
      ],
      "metadata": {
        "id": "h7CEbj1CZ_8Y"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Input the value of $n$<br>\n",
        "Initialize $sum=0$<br>\n",
        "Loop $n$ times<br>\n",
        "$\\quad$ Input a number $x$<br>\n",
        "$\\quad$ $sum+=x^2$<br>\n",
        "Print $sum$"
      ],
      "metadata": {
        "id": "kEoM0HU4aPRo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def findSumSquares():\n",
        "  n=int(input(\"Enter the value of n: \"))\n",
        "  sum=0\n",
        "  for i in range(n):\n",
        "    sum+=(i+1)**2\n",
        "  print(f\"The sum of squares of first {n} natural numbers is {sum}\")\n",
        "\n",
        "findSumSquares()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pwaYZYw_aF5l",
        "outputId": "70dfde70-2ae2-4c58-d976-bcd9e198e28e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the value of n: 5\n",
            "The sum of squares of first 5 natural numbers is 55\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Print all odd numbers between $0$ and $n$ (inclusive), where $n$ is given as input by the user."
      ],
      "metadata": {
        "id": "XQx28CaGcTEx"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Input $n$ from the user<br>\n",
        "Loop $n+1$ times incrementing $i$ from $0$ to $n$<br>\n",
        "$\\quad$ Check if $i$ is odd<br>\n",
        "$\\quad$ if $i$ is odd<br>\n",
        "$\\quad\\quad$ Print $i$"
      ],
      "metadata": {
        "id": "IUHstD_Gc0XV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def printOdd():\n",
        "  n=int(input(\"Enter a number: \"))\n",
        "  for i in range(n+1):\n",
        "    if i%2!=0:\n",
        "      print(i, end=\" \")\n",
        "\n",
        "printOdd()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bGycQR_ncZgF",
        "outputId": "5966ef68-27e1-48b1-feb9-57c03df5276e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 17\n",
            "1 3 5 7 9 11 13 15 17 "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def printOdd1():\n",
        "  n=int(input(\"Enter a number: \"))\n",
        "  for i in range(n+1):\n",
        "    if i%2==0:\n",
        "      pass\n",
        "    else:\n",
        "      print(i,end=\" \")\n",
        "\n",
        "printOdd1()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ewndJdU_eQXb",
        "outputId": "b3c94d42-4c4b-480a-b871-e53d6999c448"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 17\n",
            "1 3 5 7 9 11 13 15 17 "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def printOdd2():\n",
        "  n=int(input(\"Enter a number: \"))\n",
        "  for i in range(1,n+1,2):\n",
        "    print(i,end=\" \")\n",
        "printOdd2()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "b8U2rodifVH3",
        "outputId": "2fb23e06-597b-457c-c0f1-cb81708ebc90"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 17\n",
            "1 3 5 7 9 11 13 15 17 "
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Fibonacci Series*<br>\n",
        "The series starts with 2 numbers $0$ and $1$. The next number in the series is the sum of the previous 2 numbers<br>\n",
        "$0,1,1,2,3,5,8,13,21,34,55,89 ...$"
      ],
      "metadata": {
        "id": "e-GOgd-hgABP"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Write a program to generate the first $n$ number of the Fibonacci series, where $n$ is taken as input from the user."
      ],
      "metadata": {
        "id": "tQ9eCjDhggry"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Take as input the value of $n$<br>\n",
        "Let $f_i$ be the 1st number<br>\n",
        "Let $f_j$ be the 2nd number<br>\n",
        "Print $f_i$ and $f_j$<br>\n",
        "Loop $n-2$ times<br>\n",
        "$\\quad$ Let $f_n=f_i+f_j$<br>\n",
        "$\\quad$ Print $f_n$<br>\n",
        "$\\quad$ $f_i=f_j$<br>\n",
        "$\\quad$ $f_j=f_n$"
      ],
      "metadata": {
        "id": "HGdA7kZWhTN4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def Fibonacci():\n",
        "  n=int(input(\"Enter a number: \"))\n",
        "  f_i=0\n",
        "  f_j=1\n",
        "  print(f_i, f_j, end=\" \")\n",
        "  for i in range(n-2):\n",
        "    f_n=f_i+f_j\n",
        "    print(f_n, end=\" \")\n",
        "    f_i=f_j\n",
        "    f_j=f_n\n",
        "\n",
        "Fibonacci()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m-hb9og9gqJp",
        "outputId": "83fdb817-77be-4c77-84c0-f8d350f698ef"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 10\n",
            "0 1 1 2 3 5 8 13 21 34 "
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Indefinite Loops**"
      ],
      "metadata": {
        "id": "aqUiYiUAqJJF"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Take as input numbers from the user and find their sum. The system should prompt the user to enter a number till the user provides $-1$ as input. The value of $-1$ is not included in the sum*"
      ],
      "metadata": {
        "id": "CuCVchlcqLwn"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Initialize $sum=0$<br>\n",
        "Prompt the user to enter a number $x$<br>\n",
        "if $x!=-1$<br>\n",
        "$\\quad$ $sum+=x$<br>\n",
        "Loop till user enters $x=-1$ as input<br>\n",
        "$\\quad$ Prompt the user to enter another number $x$<br>\n",
        "$\\quad$ if $x!=-1$<br>\n",
        "$\\quad\\quad$ $sum+=x$<br>\n",
        "Print $sum$"
      ],
      "metadata": {
        "id": "MOLDGBNRqhJN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def findSum():\n",
        "  sum=0\n",
        "  count=0\n",
        "  x=eval(input(\"Enter a number (-1 to exit): \"))\n",
        "  if x!=-1:\n",
        "    sum+=x\n",
        "    count+=1\n",
        "  while x!=-1:\n",
        "    x=eval(input(\"Enter another number (-1 to exit): \"))\n",
        "    if x!=-1:\n",
        "      sum+=x\n",
        "      count+=1\n",
        "    if count!=0:\n",
        "      avg=sum/count\n",
        "    else:\n",
        "      avg=0\n",
        "  print(f\"The sum of the numbers is {sum} and average is {avg}\")\n",
        "\n",
        "findSum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8Z22ClaAsDDI",
        "outputId": "9c3c60f4-f9d7-496c-b28a-d185f315815c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number (-1 to exit): 1\n",
            "Enter another number (-1 to exit): 2\n",
            "Enter another number (-1 to exit): 3\n",
            "Enter another number (-1 to exit): 4\n",
            "Enter another number (-1 to exit): 5\n",
            "Enter another number (-1 to exit): -1\n",
            "The sum of the numbers is 15 and average is 3.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def findSum1():\n",
        "  sum=0\n",
        "  count=0\n",
        "  moreData=\"yes\"\n",
        "  while moreData==\"yes\":\n",
        "    x=eval(input(\"Enter a number: \"))\n",
        "    sum+=x\n",
        "    count+=1\n",
        "    moreData=input(\"Do you want to add more data (yes/no): \")\n",
        "\n",
        "  print(f\"The sum of the numbers is {sum} and average is {sum/count}\")\n",
        "\n",
        "findSum1()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "P_1By5VNt2rN",
        "outputId": "7d89bc3a-5697-400a-d61d-95c2f50d13e2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 1\n",
            "Do you want to add more data (yes/no): yes\n",
            "Enter a number: 2\n",
            "Do you want to add more data (yes/no): yes\n",
            "Enter a number: 3\n",
            "Do you want to add more data (yes/no): yes\n",
            "Enter a number: 4\n",
            "Do you want to add more data (yes/no): yes\n",
            "Enter a number: 5\n",
            "Do you want to add more data (yes/no): no\n",
            "The sum of the numbers is 15 and average is 3.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Nested loops**"
      ],
      "metadata": {
        "id": "ruRlxiRCu_lQ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Try to draw the following pattern:<br>\n",
        "$*\\quad *\\quad *\\quad *$<br>\n",
        "$*\\quad *\\quad *\\quad *$<br>\n",
        "$*\\quad *\\quad *\\quad *$<br>\n",
        "$*\\quad *\\quad *\\quad *$<br>\n",
        "$*\\quad *\\quad *\\quad *$<br>\n",
        "\n",
        "Here the number of rows and columns are taken as input from the user"
      ],
      "metadata": {
        "id": "0r-b47gYvDxv"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def printStars():\n",
        "  n=int(input(\"Enter the number of rows: \"))\n",
        "  m=int(input(\"Enter the number of columns: \"))\n",
        "  for i in range(n):\n",
        "    for j in range(m):\n",
        "      print(\"*\", end=\"  \")\n",
        "    print()\n",
        "\n",
        "printStars()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zWFKiUttvjpm",
        "outputId": "2586f4f5-5d7a-4df1-a47a-3126dfd5cc94"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the number of rows: 5\n",
            "Enter the number of columns: 4\n",
            "*  *  *  *  \n",
            "*  *  *  *  \n",
            "*  *  *  *  \n",
            "*  *  *  *  \n",
            "*  *  *  *  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Now try the following pattern: <br>\n",
        "$*$<br>\n",
        "$* \\quad *$<br>\n",
        "$* \\quad * \\quad *$<br>\n",
        "$* \\quad * \\quad * \\quad *$<br>\n",
        "\n",
        "Take as input only the rows $r$ from the user"
      ],
      "metadata": {
        "id": "GLswBTF4w6BF"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Consider a 3 digit number, say 153. There are 3 digits. If we raise each digit to the power of the number of digits and find the sum, the sum equals the number itself.<br>\n",
        "\n",
        "Thus $1^3+5^3+3^3=153$. Such a number is called as an Armstrong number. Given a 3 digit number, check whether the number is Armstrong or not."
      ],
      "metadata": {
        "id": "uoR7Q2ZoxzrU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def checkArmstrong():\n",
        "  x=int(input(\"Enter a 3 digit number: \"))\n",
        "  q=x\n",
        "  sum=0\n",
        "  while q>0:\n",
        "    r=q%10\n",
        "    q=q//10\n",
        "    sum+=r**3\n",
        "  if sum==x:\n",
        "    print(f\"{x} is Armstrong\")\n",
        "  else:\n",
        "    print(f\"{x} is not Armstrong\")\n",
        "\n",
        "checkArmstrong()\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LZ_uuRP9xVag",
        "outputId": "30b764f1-a625-40fd-e8ab-4679090e9cd0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a 3 digit number: 407\n",
            "407 is Armstrong\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Sequences**"
      ],
      "metadata": {
        "id": "gAJWKzvjEwFF"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Strings**"
      ],
      "metadata": {
        "id": "ozjgUo7MEyOl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "c=\"abcd\"\n",
        "type(c)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "diDbbMVQE2l1",
        "outputId": "3126040b-8257-4c4e-c3f1-47609d557ca9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "str"
            ]
          },
          "metadata": {},
          "execution_count": 1
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "String is a sequence of characters, where the position of each character is numbered by an index, starting from $0$, which is the index of the leftmost character. From left to right the index varies from $0$ to $length\\_of\\_string - 1$. One can index a string from the right as well. The righmost character has an index of -1. Here the index varies from $-1$ to $length\\_of\\_string$"
      ],
      "metadata": {
        "id": "QJbyPB_2FGfm"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(c[-4])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5hufUwhsFYsj",
        "outputId": "4fb416cd-f8c8-4b5e-8efe-89fe89e61695"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "a\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Aside from indexing the individual characters, we can also access a contiguous subsequence of characters in a string (substring). This operation is termed as slicing. Syntax is $<string>[start\\_index:end\\_index]$. This means, slicing returns the substring at the $start\\_index$ and running up to, but not including the $end\\_index$."
      ],
      "metadata": {
        "id": "BAVsuqnxGcLo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "greet=\"Hello World\"\n",
        "greet[:]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "zt88-oXBHJdR",
        "outputId": "c54a5a56-0a1d-4252-e027-11957dbaf573"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Hello World'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Concatenation and Repetition"
      ],
      "metadata": {
        "id": "cIpbn1VZHlzl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "s1=\"Hello \"\n",
        "s2=\"World\"\n",
        "s=s1+s2\n",
        "print(s)\n",
        "s3=s1*3\n",
        "print(s3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "J2TcrkGHHnzR",
        "outputId": "7a41daa3-2191-49f5-fe01-724d46a52074"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello World\n",
            "Hello Hello Hello \n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Length of a string* len(str)"
      ],
      "metadata": {
        "id": "QRfZ1NDlIa3x"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "len(s)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Gffff0kWIjG6",
        "outputId": "15c28bf7-c7e5-491d-f7f5-69ee33cc41ed"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "11"
            ]
          },
          "metadata": {},
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(len(s)):\n",
        "  print(s[i])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YzZ_gNKXIrJ4",
        "outputId": "6da1df22-3cee-4e52-a2d9-7bfaf0778d01"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "H\n",
            "e\n",
            "l\n",
            "l\n",
            "o\n",
            " \n",
            "W\n",
            "o\n",
            "r\n",
            "l\n",
            "d\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "new_str=\"\"\n",
        "for i in s:\n",
        "  if i !='o':\n",
        "    new_str+=i\n",
        "  else:\n",
        "    new_str+='0'\n",
        "print(new_str)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2JcYGSLzI_vS",
        "outputId": "bb1ac54c-47bb-44cd-abe5-be78e9959b20"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hell0 W0rld\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**String Representation**"
      ],
      "metadata": {
        "id": "eKb-v2ssIe5Z"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Computer systems use industry standard encodings to represent the characters. One of the oldest and most popularly used encoding was the ASCII (American Standard Code for Information Interchange). ACII uses the numbers 0 through 127 to represent the characters that were typically present in the keyboard. ASCII is mostly US centric. However, with growing demand to represent other language characters, an extended encoding system was setup, termed as Unicode. To derive the unicode for a character use the ord() function"
      ],
      "metadata": {
        "id": "pmDHvr4uKMj3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "ord('~')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OdzclBKhLLTi",
        "outputId": "ed542960-4f08-4253-f926-4277942f04e4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "126"
            ]
          },
          "metadata": {},
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "chr(126)"
      ],
      "metadata": {
        "id": "0FJEIc7mLgmQ",
        "outputId": "c17da33b-1722-46ce-940c-c2e026986d6d",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'~'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Strings are immutable*"
      ],
      "metadata": {
        "id": "p7Blj7I2kMn6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "greet=\"Hello World\"\n",
        "greet[1]='a'"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 159
        },
        "id": "npo8sL5ZkQzZ",
        "outputId": "6f7cb528-d335-4ce1-896f-834177f1cd72"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "'str' object does not support item assignment",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipython-input-1211170393.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mgreet\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"Hello World\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mgreet\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'a'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m: 'str' object does not support item assignment"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "greet=\"Hello World! Today is Children's Day\"\n",
        "greet.split()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "52Fro34uku5X",
        "outputId": "82d09827-481f-44a2-e04e-62d718638146"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Hello', 'World!', 'Today', 'is', \"Children's\", 'Day']"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Split a string on the basis of a given character (say @)"
      ],
      "metadata": {
        "id": "g-MOnMJGllK0"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "eid=\"abc_cde@gmail.com@abc.com\"\n",
        "eid.split('@', 2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uVYQEAjllqTR",
        "outputId": "0e86451f-58ac-45dd-c57d-9d22dd5d8d6f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['abc_cde', 'gmail.com', 'abc.com']"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Changing case in strings**"
      ],
      "metadata": {
        "id": "wgoXJWTgmXRO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "greet=\"hello world!\"\n",
        "p=greet.upper()\n",
        "p_low=p.lower()\n",
        "p_capital=greet.capitalize()\n",
        "p_title=greet.title()\n",
        "p_swap=p_title.swapcase()\n",
        "print(p_swap)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kdsWHrK5mWr-",
        "outputId": "ba30c252-9932-400a-dc22-8f68ee06e1f8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hELLO wORLD!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Trimming of the white spaces**"
      ],
      "metadata": {
        "id": "5TWHoqPGnKO7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "greet=\"       Hello World         \"\n",
        "l=greet.strip()\n",
        "le=greet.lstrip()\n",
        "ri=greet.rstrip()\n",
        "print(ri)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HSBsryoRnObx",
        "outputId": "e3c056a9-afbf-423b-ed1a-f6b81bd49dea"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "       Hello World\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Searching and Finding**"
      ],
      "metadata": {
        "id": "ACOvfp3wntxO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "words=\"madam there goes adam\"\n",
        "fo=words.find(\"adam\")\n",
        "count=words.count(\"adam\")\n",
        "prefix=words.startswith(\"adam\")\n",
        "suffix=words.endswith(\"adam\")\n",
        "print(suffix)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3dww42Ehn1yG",
        "outputId": "122ab4e2-9e4f-4b44-d527-4973861c4828"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Replace and modification**"
      ],
      "metadata": {
        "id": "VJMSBuxBouJ4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "sent=\"madam there goes adam\"\n",
        "p=sent.replace(\"adam\", \"am\")\n",
        "print(sent)\n",
        "print(p)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vJI19ru5oySn",
        "outputId": "07bc9e63-1026-4dd8-b9c3-5ff46f60b545"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "madam there goes adam\n",
            "mam there goes am\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Padding**"
      ],
      "metadata": {
        "id": "OxJOh6wWpX8p"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "greet=\"Hello World!\"\n",
        "p=greet.center(50)\n",
        "la=greet.ljust(50)\n",
        "ra=greet.rjust(50)\n",
        "print(ra, end=\"\")\n",
        "print(\"!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mybGAucuphQq",
        "outputId": "00e22737-6054-4b46-ff37-a071b513cd03"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                                      Hello World!!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Checking the string characteristics**"
      ],
      "metadata": {
        "id": "dCuxkaNSqLcO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "greet=\"Hell0 World!\"\n",
        "print(greet.isalpha()) #Check whether all the characters in the string is alphabetic\n",
        "print(greet.isdigit())\n",
        "print(greet.isalnum())\n",
        "print(greet.isspace())\n",
        "print(greet.isupper())\n",
        "print(greet.islower())\n",
        "print(greet.istitle())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5XoO9GJcqP6z",
        "outputId": "2d1d83e8-dfde-4541-d75a-50fc948c0bfa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n",
            "False\n",
            "False\n",
            "False\n",
            "False\n",
            "False\n",
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Assignment 3**"
      ],
      "metadata": {
        "id": "55K4328fAOv9"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. GCD<br>\n",
        "$15)35(2$<br>\n",
        "   $30$<br>\n",
        "   $---$<br>\n",
        "    $5)15(3$<br>\n",
        "      15\n",
        "      ---\n",
        "      XX"
      ],
      "metadata": {
        "id": "qq8li2PGARib"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def findGCD():\n",
        "  b=int(input(\"Enter the larger number: \"))\n",
        "  a=int(input(\"Enter the other number: \"))\n",
        "  while a>0:\n",
        "    b,a=a,b%a\n",
        "    if b%a==0:\n",
        "      gcd=a\n",
        "      break\n",
        "  print(f\"The GCD is {gcd}\")\n",
        "\n",
        "findGCD()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mtr-Xo3LA0_C",
        "outputId": "1385f92e-513a-4e47-9adb-e03dc3f5fb42"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the larger number: 35\n",
            "Enter the other number: 15\n",
            "The GCD is 5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def checkPalindrome():\n",
        "  p=input(\"Enter a string: \")\n",
        "  flag=True\n",
        "  for i in range(len(p)):\n",
        "    if p[i]!=p[-1-i]:\n",
        "      flag=False\n",
        "      break\n",
        "\n",
        "  if flag==True:\n",
        "    print(f\"{p} is a palindrome\")\n",
        "  else:\n",
        "    print(f\"{p} is not a palindrome\")\n",
        "\n",
        "checkPalindrome()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LTpTILFjErs4",
        "outputId": "8e073329-0512-4c39-ed34-875597388ee7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a string: madame\n",
            "madame is not a palindrome\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def checkPallin(p):\n",
        "  og=p\n",
        "  rev=0\n",
        "  while p>0:\n",
        "    d=p%10\n",
        "    rev=rev*10+d\n",
        "    p//=10\n",
        "\n",
        "  if rev==og:\n",
        "     print(f\"{og} is a Pallindrome\")\n",
        "  else:\n",
        "      print(f\"{og} is not a Pallindrome\")\n",
        "\n",
        "def main():\n",
        "    p=int(input(\"Enter a number: \"))\n",
        "    checkPallin(p)\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pwL_hTlWGblw",
        "outputId": "c1b5809c-3867-4bb8-b0a8-56d7b9cf61e4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 12321\n",
            "12321 is a Pallindrome\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def printPyramid():\n",
        "  r=int(input(\"Enter the number of rows: \"))\n",
        "  for i in range(1, r + 1):\n",
        "    print(\" \" *(r-i), end=\"\")\n",
        "\n",
        "    for j in range(1, i + 1):\n",
        "     print(j, end=\"\")\n",
        "\n",
        "    for j in range(i - 1, 0, -1):\n",
        "      print(j, end=\"\")\n",
        "\n",
        "    print()\n",
        "\n",
        "printPyramid()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hoRzPW7GINNi",
        "outputId": "ab744c0e-74b7-4fac-fe1f-4988b6cb8784"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the number of rows: 8\n",
            "       1\n",
            "      121\n",
            "     12321\n",
            "    1234321\n",
            "   123454321\n",
            "  12345654321\n",
            " 1234567654321\n",
            "123456787654321\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "Eusfe8UaJt-t"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def findAP():\n",
        "  a=int(input(\"Enter first term(a): \"))\n",
        "  n=int(input(\"Enter number of terms(n): \"))\n",
        "  d=int(input(\"Enter common difference(d): \"))\n",
        "  sum=0\n",
        "  #print(\"The AP series is: \", end=\"\")\n",
        "  for i in range(n):\n",
        "    term = a+i*d\n",
        "    if i<n-1:\n",
        "      print(f\"{term} +\", end=\" \")\n",
        "    else:\n",
        "      print(f\"{term} = \", end=\" \")\n",
        "    sum+=term\n",
        "  print(sum)\n",
        "\n",
        "findAP()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Rng7AfG7IP0q",
        "outputId": "5f4e2346-2b8d-4c96-c509-cd3c838dbde2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter first term(a): 1\n",
            "Enter number of terms(n): 10\n",
            "Enter common difference(d): 4\n",
            "1 + 5 + 9 + 13 + 17 + 21 + 25 + 29 + 33 + 37 =  190\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Lists in python**"
      ],
      "metadata": {
        "id": "UXC-0AHSjUME"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Strings are sequence of characters, Lists, on the other hand are sequences of arbitrary objects"
      ],
      "metadata": {
        "id": "WU8rTbQJjYV7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "myList1=[1,2,3]\n",
        "myList2=[1,2,3.4,'c',\"hello\"]\n",
        "myList3=[2*3, 6*5]\n",
        "print(myList3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QSns_Dwcjs_i",
        "outputId": "08797b4e-ae1d-461c-d9e2-4c91f0fac96b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[6, 30]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*List comprehension*"
      ],
      "metadata": {
        "id": "xsh4G_yKkZRM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "myList4=[x**2 for x in range(5)]\n",
        "print(myList4)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j0y_126fkPoC",
        "outputId": "ec8da807-e1b3-44e6-f692-3ac3e8fb35c8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0, 1, 4, 9, 16]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "myList5=list(x+1 for x in range(1,6))\n",
        "print(myList5)\n",
        "type(myList5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JRckSxbckk6m",
        "outputId": "d5142175-c7d4-44ed-9d1f-286d592145bd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[2, 3, 4, 5, 6]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "list"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "L1=[1,2,3]\n",
        "L2=[1,2,3]\n",
        "L1==L2\n",
        "L1 is L2"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cX_U0ljplFBI",
        "outputId": "1f193885-5882-4871-f49b-40c6a3bb6f6e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "L1=L2=[1,2,3,4,5]\n",
        "L1 is L2"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MNKBrau9lURz",
        "outputId": "d64e36bf-014b-4cd7-d9a0-79c933394fdd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "len(L1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ce99C7XLleMr",
        "outputId": "f4453463-6833-4666-be50-022554db15b0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "5"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Indexing, concatenating and repeating lists*"
      ],
      "metadata": {
        "id": "OzRPLOb4lplZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(L1[2])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3VXQp2ralvS8",
        "outputId": "5a205982-aadb-46f5-8f27-fdb9e3993713"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "L1=[1,2,3]\n",
        "L2=['a', 'b','c']\n",
        "print(L1+L2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pQnl1li3l3Be",
        "outputId": "7cbb1ac2-7e4d-4a5c-bc54-b038d5e5f2dc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3, 'a', 'b', 'c']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(L1*2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RMJ5fgRKmBnW",
        "outputId": "371447a3-03cc-4048-c604-1dbfbd90a820"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3, 1, 2, 3]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Slicing in lists*"
      ],
      "metadata": {
        "id": "ya2uHw4zmFwO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "L1=[1,2,3,4,5,6,7,8]\n",
        "L1[1:9:2]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ENJ3lfbemK--",
        "outputId": "75eafa23-37d5-42b0-c105-c75d5f639d55"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[2, 4, 6, 8]"
            ]
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "L1[1:]\n",
        "L1[:7]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "h_xq4w9SmuLK",
        "outputId": "d358589f-c427-4e8a-d881-74052a1b2539"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1, 2, 3, 4, 5, 6, 7]"
            ]
          },
          "metadata": {},
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "L1[-1::-1]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WXzVsiLtminM",
        "outputId": "870552f8-5f93-4335-d6ea-c2727232033c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[8, 7, 6, 5, 4, 3, 2, 1]"
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Unlike strings lists are mutable"
      ],
      "metadata": {
        "id": "ZGNAuTjBnSvE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "L1[7]='a'\n",
        "print(L1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LTFgsqh8neX0",
        "outputId": "b1b3a5ef-fa0d-4475-f227-03ea4263d153"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3, 4, 5, 6, 7, 'a']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Iterating over the elements of a list"
      ],
      "metadata": {
        "id": "TEXT0JI2noFy"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "for i in L1:\n",
        "  print(i, end=\" \")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Vx0SVM3VnrQP",
        "outputId": "e30cf000-a4ea-46f4-cd81-93dd04d99a1a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3 4 5 6 7 a "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(len(L1)):\n",
        "  print(L1[i], end=\" \")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CQvkbBSJn0mb",
        "outputId": "bbde5134-19ec-4dcd-de3f-0cbd3c5682f6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3 4 5 6 7 a "
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Multidimensional lists*"
      ],
      "metadata": {
        "id": "inHThhfKoFqi"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "ML1=[[1,2,3], [4,5,6], [7,8,9]]\n",
        "print(ML1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MMx2U6RfoJbX",
        "outputId": "745af164-7c63-43b1-bc33-6571ad509d31"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1, 2, 3], [4, 5, 6], [7, 8, 9]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "ML1[0][2]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ytdh3AuWoera",
        "outputId": "f07b7600-ba93-4fb0-dff3-ae57145f79de"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3"
            ]
          },
          "metadata": {},
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Accessing elements of a multidimensional list using loops*"
      ],
      "metadata": {
        "id": "YKC6FvM4o656"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "for i in ML1:\n",
        "  for j in i:\n",
        "    print(j, end=\" \")\n",
        "  print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NANe8H2fpAeo",
        "outputId": "5d012722-fc07-4543-c24f-2ffbf584c495"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3 \n",
            "4 5 6 \n",
            "7 8 9 \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(len(ML1)):\n",
        "  for j in range(len(ML1[i])):\n",
        "    print(ML1[i][j], end=\" \")\n",
        "  print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Rhc8yVYQpcgn",
        "outputId": "59756caf-13aa-4186-e069-9d0b0a918d12"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3 \n",
            "4 5 6 \n",
            "7 8 9 \n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Adding elements to a list*"
      ],
      "metadata": {
        "id": "wQ04leddqImS"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "L2=[]\n",
        "L2.append(1)\n",
        "L2.append('a')\n",
        "print(L2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8ZWrGnICqMOc",
        "outputId": "27fbb8da-eb15-40cb-a944-71d5a73b33ea"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 'a']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for x in range(5):\n",
        "  L2.append(x+1)\n",
        "print(L2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "If8qEVfNqX_p",
        "outputId": "ef3c8249-311e-4268-c40f-146673e620d7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 'a', 1, 2, 3, 4, 5]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Append elements of a list to another list*"
      ],
      "metadata": {
        "id": "sF-xfAZ0qlAe"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "L1=[\"Hello\", \"World\"]\n",
        "L1.extend(L2)\n",
        "print(L1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "a4bKYPoxqqAM",
        "outputId": "0fbf909e-c2c6-42ff-a350-71126aca095c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Hello', 'World', 1, 'a', 1, 2, 3, 4, 5]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Inserting an element at a given position"
      ],
      "metadata": {
        "id": "ommF7SADrN_W"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "L1.insert(0,\"Hi!!! \")\n",
        "print(L1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "U5N2q1YOrRaK",
        "outputId": "413ac68d-6611-460d-ad3c-f760012bfb53"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Hi!!! ', 'Hello', 'World', 1, 'a', 1, 2, 3, 4, 5]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Removing elements from the list"
      ],
      "metadata": {
        "id": "ZasDkQhvrehU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "L1.remove('a')\n",
        "print(L1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "B6zTNBFprh5w",
        "outputId": "7251340c-4cf5-4867-cc63-2635248f837e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Hi!!! ', 'Hello', 'World', 1, 1, 2, 3, 4, 5]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "L1.pop(0)\n",
        "print(L1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZHFUXqxarpiz",
        "outputId": "9fb93e13-3942-4578-aa8d-dd2ae784d7db"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Hello', 'World', 1, 1, 2, 3, 4, 5]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Take 2 matrices of dimesion $3\\times 2$ as input from the user. Find the sum of the 2 matrices and print"
      ],
      "metadata": {
        "id": "iEISPDshr5yN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def createMatrix():\n",
        "  M=[]\n",
        "  for i in range(3):\n",
        "    rowList=[]\n",
        "    for j in range(2):\n",
        "      p=int(input(\"Enter an element: \"))\n",
        "      rowList.append(p)\n",
        "    M.append(rowList)\n",
        "  return(M)\n",
        "\n",
        "def findMatrixSum(m1,m2):\n",
        "  sum=[[0,0],[0,0],[0,0]]\n",
        "  for i in range(3):\n",
        "    for j in range(2):\n",
        "      sum[i][j]=m1[i][j]+m2[i][j]\n",
        "  return(sum)\n",
        "\n",
        "\n",
        "def main():\n",
        "  m1=createMatrix()\n",
        "  m2=createMatrix()\n",
        "  sumMatrix=findMatrixSum(m1,m2)\n",
        "  print(f\"The resultant sum matrix is {sumMatrix}\")\n",
        "\n",
        "main()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "np7CoOd8sCzf",
        "outputId": "555e5f6d-031c-4fc9-c414-4e9fee48b90c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter an element: 1\n",
            "Enter an element: 2\n",
            "Enter an element: 3\n",
            "Enter an element: 4\n",
            "Enter an element: 5\n",
            "Enter an element: 6\n",
            "Enter an element: 1\n",
            "Enter an element: 2\n",
            "Enter an element: 3\n",
            "Enter an element: 4\n",
            "Enter an element: 5\n",
            "Enter an element: 6\n",
            "The resultant sum matrix is [[2, 4], [6, 8], [10, 12]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Lists are sequences of arbitrary objects."
      ],
      "metadata": {
        "id": "_IPsiCD9tziz"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Tuples**"
      ],
      "metadata": {
        "id": "pRjmEse-t27M"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Tuples are similar to lists, but are immutable. Once created cannot be modified."
      ],
      "metadata": {
        "id": "wlNHazsqt5X0"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "l1=[]  #Creating lists\n",
        "t1=(1,2,3)\n",
        "print(t1)\n",
        "type(t1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GqqMQBgHuDMM",
        "outputId": "b559fb14-4446-4a46-be51-bf258e58e971"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(1, 2, 3)\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tuple"
            ]
          },
          "metadata": {},
          "execution_count": 1
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Like lists, tuples can:<br>\n",
        "Contain any and different types of elements<br>\n",
        "Contain duplicate elements like t1=(1,1,1,3)<br>\n",
        "Be indexed exactly in the same way as lists, like t1[0], t1[1], ...<br>\n",
        "Be sliced exactly in the same way as lists $t1[1:5:2]$<br>\n",
        "Be concatenated like t3=t1+t2<br>\n",
        "Be repeated like t3=t1*2<br>\n",
        "Be nested like $t2=(1,2,3, (1,2,3))$<br>\n",
        "Be passed to a function, and will result in pass-by-value rather than pass-by-reference (as in the case of lists)<br>\n",
        "Be iterated over"
      ],
      "metadata": {
        "id": "wczlBdL8uYYh"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Difference between pass by value and pass by reference"
      ],
      "metadata": {
        "id": "iDiPh_qPv69g"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def changeValue(t):\n",
        "  print(f\"Value in function before change {t}\")\n",
        "  t=5\n",
        "  print(f\"Value in function after change {t}\")\n",
        "\n",
        "def main():\n",
        "  p=3\n",
        "  changeValue(p)\n",
        "  print(p)\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GVM7SQrJymm4",
        "outputId": "6457cc97-80a8-4238-968b-d66cb4fefba4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Value in function before change 3\n",
            "Value in function after change 5\n",
            "3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def changeList(myList):\n",
        "  myList[0]=\"New Element\"\n",
        "\n",
        "def main():\n",
        "  l1=[1,2,3,4]\n",
        "  changeList(l1)   #Will change the first element of the list passed\n",
        "  print(l1)\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KyUlWFDzv-05",
        "outputId": "44f53cac-ca4c-45f3-8f05-0ecb89de649d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['New Element', 2, 3, 4]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "t3=(1,2,3,\"abc\")\n",
        "for i in t3:\n",
        "  print(i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2CJs5yNj0LGq",
        "outputId": "6cd2d7e0-9a7e-45c1-cc4b-3d7a3d3e3096"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "abc\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "t4=((1,2,3), (4,5,6), (7,8,9))\n",
        "for i in t4:\n",
        "  for j in i:\n",
        "    print(j, end=\" \")\n",
        "  print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KFwJ2NZP0ZOg",
        "outputId": "ca52fcaf-3598-4480-f495-293bf1faf58d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3 \n",
            "4 5 6 \n",
            "7 8 9 \n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Dictionaries**"
      ],
      "metadata": {
        "id": "sn_8whAE0ut7"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Both lists and tuples are indexed using numerical indices $t1[0], t1[1]$. However, what if we want to store index with non-numerical values?<br>\n",
        "Python allows this. We can use a dictionary to store elements with keys of any types (not necessarily integers), and values of any types as well."
      ],
      "metadata": {
        "id": "VAt1nGZB0yvk"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dict={\"Key1\":12, \"Key2\":13, \"Key1\": 14}\n",
        "#dict[\"Key2\"]=15\n",
        "dict"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nROiF5jA1Tuv",
        "outputId": "9dd1ac66-2cb7-4e69-9d85-e6c46d3d0943"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'Key1': 14, 'Key2': 13}"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "In dictionaries, the keys must be unique, values can be same."
      ],
      "metadata": {
        "id": "RNwR8Dai1-hd"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Unlike lists<br>\n",
        "dictionaries CANNOT be concatenated<br>\n",
        "CANNOT be repeated<br>\n",
        "\n",
        "Can be nested<br>\n",
        "Can be passed to a function using pass-by-reference"
      ],
      "metadata": {
        "id": "oEDOgERS2DEF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dict2={\"k1\":{\"k11\":1, \"k12\":2, \"k13\":3}, \"k2\":{\"k21\":4, \"k22\":5, \"k23\":6}}\n",
        "dict2"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BplWbsCk2PiV",
        "outputId": "95596750-0a3f-4382-9d19-f11179a37304"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'k1': {'k11': 1, 'k12': 2, 'k13': 3}, 'k2': {'k21': 4, 'k22': 5, 'k23': 6}}"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Dictionaries can be iterated"
      ],
      "metadata": {
        "id": "lI40JPPT2u7G"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "for i in dict2:\n",
        "  for j in dict2[i]:\n",
        "    print(f\"{j} {dict2[i][j]}\", end=\" \")\n",
        "  print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tSPommxb2uPI",
        "outputId": "39646cd3-5dbd-4719-bb8a-9cf2831d560c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "k11 1 k12 2 k13 3 \n",
            "k21 4 k22 5 k23 6 \n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Adding elements to a dictionary"
      ],
      "metadata": {
        "id": "Z-PohO7l4DRx"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dict2[\"k3\"]={\"k31\":7, \"k32\":8, \"k33\":9}\n",
        "dict2"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0WRHx31C4Fn_",
        "outputId": "32087697-1798-478e-a01b-946ba632301d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'k1': {'k11': 1, 'k12': 2, 'k13': 3},\n",
              " 'k2': {'k21': 4, 'k22': 5, 'k23': 6},\n",
              " 'k3': {'k31': 7, 'k32': 8, 'k33': 9}}"
            ]
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Deleting elements to a dictionary"
      ],
      "metadata": {
        "id": "TNBaYJkO4boS"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dict2[\"k4\"]=(1,2)\n",
        "dict2[\"k5\"]=(3,4)\n",
        "dict2"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4l-7d9mU4j4C",
        "outputId": "8a810962-318e-453e-eb0a-8e605eda3ec8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'k1': {'k11': 1, 'k12': 2, 'k13': 3},\n",
              " 'k2': {'k21': 4, 'k22': 5, 'k23': 6},\n",
              " 'k3': {'k31': 7, 'k32': 8, 'k33': 9},\n",
              " 'k4': (1, 2),\n",
              " 'k5': (3, 4)}"
            ]
          },
          "metadata": {},
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "del dict2[\"k5\"]\n",
        "dict2"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "F6KOeHQV4us5",
        "outputId": "6f5a0c0f-edd8-4a21-c6c6-66630b516558"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'k1': {'k11': 1, 'k12': 2, 'k13': 3},\n",
              " 'k2': {'k21': 4, 'k22': 5, 'k23': 6},\n",
              " 'k3': {'k31': 7, 'k32': 8, 'k33': 9},\n",
              " 'k4': (1, 2)}"
            ]
          },
          "metadata": {},
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dict2.pop(\"k4\")\n",
        "print(dict2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Qw_qPkdI5Arg",
        "outputId": "9273846b-f913-4405-e51d-07ef3bcde7a1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'k1': {'k11': 1, 'k12': 2, 'k13': 3}, 'k2': {'k21': 4, 'k22': 5, 'k23': 6}, 'k3': {'k31': 7, 'k32': 8, 'k33': 9}}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dict2.clear()  #Remove all the elements from the dictionary\n",
        "dict2.copy()   #Return a copy of the dictionary\n",
        "dict2.items()  #Returns a list containing a tuple for each key value pair in the dictionary\n",
        "dict2.keys()   #Returns a list of all the keys in the dictionary\n",
        "dict2.get(\"k1\") #Return  the value of the key \"k1\""
      ],
      "metadata": {
        "id": "l8bFZYz75KIB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "dict3={1:1,2:12,3:14,4:16,8:133}\n",
        "#Check whether this dictionary contains a key (say 15)\n",
        "l1=dict3.keys()\n",
        "print(l1)\n",
        "flag=False\n",
        "for i in l1:\n",
        "  if i==15:\n",
        "    print(\"Found\")\n",
        "    flag=True\n",
        "if flag==False:\n",
        "  print(\"Not found\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TZyRkBNn5qDF",
        "outputId": "e62b2b65-38a4-423c-817e-9801b2c585e7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "dict_keys([1, 2, 3, 4, 8])\n",
            "Not found\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "if 15 in l1:\n",
        "  print(\"FOund\")\n",
        "else:\n",
        "  print(\"Not found\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qWAgB9ER7CEk",
        "outputId": "f88099e9-38df-4ebd-f2a9-b34eabbae072"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Not found\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Create a dictionary to store all the students marks in each of the 5 subjects, where the key would be the student roll number.<br>\n",
        "Using the dictionary find out the average marks obtained by the students in a particular subject<br>\n",
        "FInd the median marks in given subject<br>\n",
        "List all the students who have failed ($<35$) in a given subject"
      ],
      "metadata": {
        "id": "0qFMrS2I7O9Q"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Recursion**"
      ],
      "metadata": {
        "id": "wb_QaHpvEQ6o"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def fact_iter(n):\n",
        "  fact=1\n",
        "  while(n>0):\n",
        "    fact*=n\n",
        "    n-=1\n",
        "  return(fact)"
      ],
      "metadata": {
        "id": "M7E5s_WLERhX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "p=fact_iter(5)\n",
        "print(p)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lQ8vTIBvHLPx",
        "outputId": "2449375a-0c71-4c34-f971-0c288ef149d8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "120\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def fact_rec(n):\n",
        "  if n==0:\n",
        "    return 1\n",
        "  else:\n",
        "    return n*fact_rec(n-1)"
      ],
      "metadata": {
        "id": "R1kqUg1_Ha6R"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Fibonacci Series*"
      ],
      "metadata": {
        "id": "LtO1ad-uLWWU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def fib_rec(n):\n",
        "  if n==1:\n",
        "    return 0\n",
        "  elif n==2:\n",
        "    return 1\n",
        "  else:\n",
        "    return fib_rec(n-1)+fib_rec(n-2)"
      ],
      "metadata": {
        "id": "dhYCtis_LYdL"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1,11):\n",
        "  print(fib_rec(i), end=\" \")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PA0Sl4OLLq_d",
        "outputId": "1612f30d-86ab-4d62-bc1f-1b385d3e87a5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0 1 1 2 3 5 8 13 21 34 "
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "GCD"
      ],
      "metadata": {
        "id": "6nj0C59eMEhU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def gcd_rec(a,b):\n",
        "  if b%a==0:\n",
        "    return a\n",
        "  else:\n",
        "    return gcd_rec(b%a, a)"
      ],
      "metadata": {
        "id": "KYqRUGWJNa8G"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(gcd_rec(15,35))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X8lxqLuSNuLN",
        "outputId": "bab59a0d-4be3-4076-f000-efae4e91e496"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Lab Assignments 21.11.2015**"
      ],
      "metadata": {
        "id": "a4yKljCyYeg3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def checkAnagram(s1,s2):\n",
        "    #s1=s1.replace(\" \",\"\")\n",
        "    s1=s1.lower()\n",
        "    #s2=s2.replace(\" \",\"\")\n",
        "    s2=s2.lower()\n",
        "    s1=sorted(s1)\n",
        "    s2=sorted(s2)\n",
        "    print(s1, s2)\n",
        "    if s1==s2:\n",
        "        return True\n",
        "    else:\n",
        "        return False\n",
        "\n",
        "def main():\n",
        "    s1=input(\"Enter a string: \")\n",
        "    s2=input(\"Enter the other string: \")\n",
        "    if checkAnagram(s1,s2)==True:\n",
        "        print(f\"{s1} and {s2} are anagrams\")\n",
        "    else:\n",
        "        print(\"Not Anagrams\")\n",
        "main()"
      ],
      "metadata": {
        "id": "EFU2roYcYi4d"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def checkIsomorphic(s1,s2):\n",
        "    if len(s1)!=len(s2):\n",
        "        return False\n",
        "    dict={}\n",
        "    for i in range(len(s1)):\n",
        "        a=s1[i]\n",
        "        b=s2[i]\n",
        "        if a not in dict:\n",
        "            if b in dict.values():\n",
        "                return False\n",
        "            else:\n",
        "                dict[a]=b\n",
        "        else:\n",
        "            if dict[a]!=b:\n",
        "                return False\n",
        "    return True\n",
        "\n",
        "def main():\n",
        "    s1=input(\"Enter 1st string: \")\n",
        "    s2=input(\"Enter 2nd string: \")\n",
        "    if checkIsomorphic(s1,s2)==True:\n",
        "        print(f\"{s1} and {s2} are isomorphic\")\n",
        "    else:\n",
        "        print(\"Not Isomorphic\")\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "id": "o7S0JDzlYnOa"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def matrixProduct(M1,M2):\n",
        "    C=[]\n",
        "    for i in range(len(M1)):\n",
        "        C_r=[]\n",
        "        for j in range(len(M2[0])):\n",
        "            sum=0\n",
        "            for k in range(len(M1[0])):\n",
        "                sum+=M1[i][k]*M2[k][j]\n",
        "            C_r.append(sum)\n",
        "        C.append(C_r)\n",
        "            #print(sum)\n",
        "    print(C)\n",
        "\n",
        "def main():\n",
        "    M1=[]\n",
        "    M2=[]\n",
        "    a_r=int(input(\"Enter the number of rows of a: \"))\n",
        "    a_c=int(input(\"Enter the number of cols of a: \"))\n",
        "\n",
        "    b_r=a_c\n",
        "    b_c=int(input(\"Enter the number of cols of b: \"))\n",
        "    print(\"Enter data for matrix a\")\n",
        "    for i in range(a_r):\n",
        "        Ma=[]\n",
        "        for j in range(a_c):\n",
        "            c=int(input())\n",
        "            Ma.append(c)\n",
        "        M1.append(Ma)\n",
        "    print(f\"Matrix a is {M1}\")\n",
        "    print(\"Enter data for matrix b\")\n",
        "    for i in range(b_r):\n",
        "        Mb=[]\n",
        "        for j in range(b_c):\n",
        "            c=int(input())\n",
        "            Mb.append(c)\n",
        "        M2.append(Mb)\n",
        "    print(f\"Matrix b is {M2}\")\n",
        "    print(\"\\n\\nPrinting product matrix\")\n",
        "    matrixProduct(M1,M2)\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "id": "4B2aw2HQYuVU"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def findSum(L,i):\n",
        "    if i==len(L)-1:\n",
        "        return L[i]\n",
        "    else:\n",
        "        return L[i]+findSum(L,i+1)\n",
        "\n",
        "def main():\n",
        "    L=[1,2,3,4,5,6]\n",
        "    print(findSum(L,0))\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "id": "fj44pW8PZKvJ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def THanoi(n, frm,inter,to):\n",
        "    if n==1:\n",
        "        print(f\"Move from {frm} to {to}\")\n",
        "        return\n",
        "    else:\n",
        "        THanoi(n-1,frm,to,inter)\n",
        "        print(f\"Move from {frm} to {to}\")\n",
        "        THanoi(n-1, inter,frm,to)\n",
        "\n",
        "THanoi(5,\"A\",\"B\",\"C\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "G1ZU37DmZNFn",
        "outputId": "09f8bc91-c04b-4e39-a87c-2db029833fb2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Move from A to C\n",
            "Move from A to B\n",
            "Move from C to B\n",
            "Move from A to C\n",
            "Move from B to A\n",
            "Move from B to C\n",
            "Move from A to C\n",
            "Move from A to B\n",
            "Move from C to B\n",
            "Move from C to A\n",
            "Move from B to A\n",
            "Move from C to B\n",
            "Move from A to C\n",
            "Move from A to B\n",
            "Move from C to B\n",
            "Move from A to C\n",
            "Move from B to A\n",
            "Move from B to C\n",
            "Move from A to C\n",
            "Move from B to A\n",
            "Move from C to B\n",
            "Move from C to A\n",
            "Move from B to A\n",
            "Move from B to C\n",
            "Move from A to C\n",
            "Move from A to B\n",
            "Move from C to B\n",
            "Move from A to C\n",
            "Move from B to A\n",
            "Move from B to C\n",
            "Move from A to C\n"
          ]
        }
      ]
    }
  ]
}