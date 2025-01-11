<template>
  <div class="bg-gray-50 rounded-xl shadow-inner p-6 space-y-3">
    <div class="flex justify-between items-center">
      <span class="text-sm font-medium text-gray-600">Password Strength</span>
      <span class="text-sm font-medium px-3 py-1 rounded-full" :class="strengthBadgeColor">
        {{ strengthText }}
      </span>
    </div>
    <div class="h-2 w-full bg-gray-200 rounded-full overflow-hidden">
      <div
        class="h-full transition-all duration-500 ease-out"
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
        0: 'bg-red-500',
        1: 'bg-orange-500',
        2: 'bg-yellow-500',
        3: 'bg-blue-500',
        4: 'bg-green-500'
      }
      return colors[this.strength]
    },
    strengthBadgeColor() {
      const colors = {
        0: 'bg-red-100 text-red-800',
        1: 'bg-orange-100 text-orange-800',
        2: 'bg-yellow-100 text-yellow-800',
        3: 'bg-blue-100 text-blue-800',
        4: 'bg-green-100 text-green-800'
      }
      return colors[this.strength]
    }
  }
}
</script>
