import '../styles/globals.css'
import type { AppProps } from 'next/app'
import NavBar from '../components/NavBar'

function MyApp({ Component, pageProps }: AppProps) {
  return <div className='w-screen h-screen bg-yellow-800 pl-40 pr-40 pt-10'>
    <NavBar />
    <Component {...pageProps} />
  </div>
}

export default MyApp
