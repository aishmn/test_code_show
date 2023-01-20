import { extendTheme } from '@chakra-ui/react'
import { inputAnatomy } from '@chakra-ui/anatomy'
import { createMultiStyleConfigHelpers, defineStyle } from '@chakra-ui/react'

const fonts = { mono: `'Menlo', monospace` }

const breakpoints = {
  sm: '40em',
  md: '52em',
  lg: '64em',
  xl: '80em',
  xxl: '100em'
}

const theme = extendTheme({
  semanticTokens: {
    colors: {
      text: {
        default: '#16161D',
        _dark: '#ade3b8',
      },
    },
    radii: {
      button: '12px',
    },
  },
  colors: {
    black: '#16161D',
  },
  wordBreak:{
    default:'break-word'
  },
  components:{
    Button:{
      baseStyle:{
        "background":'#9f4ac7',
        "color":"white",
      }
    }
    
  },
  styles:{
    global:{
      '*':{
        "word-break":"break-word"
      }
    }
  },
  fonts,
  breakpoints,
  config:{
    initialColorMode: 'dark',
    useSystemColorMode: false,
  }
})

//Input Field


// const { definePartsStyle, defineMultiStyleConfig } =
//   createMultiStyleConfigHelpers(inputAnatomy.keys)

// const xl = defineStyle({
//   fontSize: 'lg',
//   px: '4',
//   h: '12',
// })

// const sizes = {
//   xl: definePartsStyle({ field: xl, addon: xl }),
// }

// export const inputTheme = defineMultiStyleConfig({ sizes })


export default theme
