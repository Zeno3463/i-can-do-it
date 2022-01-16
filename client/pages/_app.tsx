import '../styles/globals.css'
import type { AppProps } from 'next/app'
import NavBar from '../components/NavBar'

function MyApp({ Component, pageProps }: AppProps) {
  return <div className='w-screen h-screen bg-yellow-800 lg:pl-40 lg:pr-40 lg:pt-10 flex flex-col'>
    <NavBar />
    <Component {...pageProps} />
  </div>
}

export default MyApp
