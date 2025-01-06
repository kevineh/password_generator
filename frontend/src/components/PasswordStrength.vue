
<template>
  <div class="space-y-2">
    <div class="flex justify-between items-center">
      <span class="text-sm text-gray-600">Password Strength</span>
      <span class="text-sm font-medium" :class="strengthColor">{{ strengthText }}</span>
    </div>
    <div class="h-2 w-full bg-gray-200 rounded-full">
      <div
        class="h-full rounded-full transition-all duration-300"
        :class="strengthColor"
        :style="{ width: `${strengthPercentage}%` }"
      ></div>
    </div>
  </div>
</template>

<script>
import zxcvbn from 'zxcvbn'

export default {
  name: 'PasswordStrength',
  props: {
    password: {
      type: String,
      required: true
    }
  },
  computed: {
    strength() {
      if (!this.password) return 0
      return zxcvbn(this.password).score
    },
    strengthPercentage() {
      return (this.strength / 4) * 100
    },
    strengthText() {
      const texts = ['Very Weak', 'Weak', 'Fair', 'Good', 'Strong']
      return texts[this.strength]
    },
    strengthColor() {
      const colors = {
        0: 'text-red-500 bg-red-500',
        1: 'text-orange-500 bg-orange-500',
        2: 'text-yellow-500 bg-yellow-500',
        3: 'text-blue-500 bg-blue-500',
        4: 'text-green-500 bg-green-500'
      }
      return colors[this.strength]
    }
  }
}
</script>
