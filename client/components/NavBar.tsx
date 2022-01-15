import React from 'react'
import Link from 'next/link'

const NavBar = () => {
	return (
		<div className='bg-amber-600 flex justify-between p-5 rounded-full shadow-2xl'>
			<Link href="/">
				<h1 className='text-neutral-200 text-3xl m-1 hover:cursor-pointer'>I <strong>Can</strong> Do It</h1>
			</Link>
			<ul className='flex justify-around text-orange-200'>
				<li className='m-3 hover:cursor-pointer hover:text-orange-300'>
					<Link href="/about">About</Link>
				</li>
				<li className='m-3 hover:cursor-pointer hover:text-orange-300'>
					<a href="http://127.0.0.1:5000/" target="_blank">API</a>
				</li>
				<li className='m-3 hover:cursor-pointer hover:text-orange-300'>
					<a href="https://github.com/Zeno3463/i-can-do-it" target="_blank">Repo</a>
				</li>
			</ul>
		</div>
	)
}

export default NavBar
