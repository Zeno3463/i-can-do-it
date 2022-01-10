import type { NextPage } from 'next'
import { GetStaticProps, InferGetStaticPropsType } from 'next';

const Home: NextPage = ({ data }: InferGetStaticPropsType<typeof getStaticProps>) => {
	return (
		<div>
			{data.map((item: any) => <div>{item}</div>)}
		</div>
	)
}

export const getStaticProps: GetStaticProps = async () => {
	const res = await fetch("http://127.0.0.1:5000/get_random/10");
	const data = await res.json();

	if (!data) return { notFound: true };
	return {
		props: { data },
	}
}

export default Home
