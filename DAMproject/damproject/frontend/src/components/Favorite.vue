<!--<template>-->
<!--  <div class="favorite">-->
<!--  &lt;!&ndash; Banner &ndash;&gt;-->
<!--		<section id="banner" data-video="images/banner">-->
<!--			<div class="inner">-->
<!--				<header>-->
<!--					&lt;!&ndash; 用户头像 &ndash;&gt;-->
<!--					<span class="avatar"><img src="../assets/images/avatar.jpg" alt=""/></span>-->
<!--          &lt;!&ndash; 用户名 调state &ndash;&gt;-->
<!--					<h1>{{this.$store.state.user_name}}</h1>-->
<!--&lt;!&ndash;					<p>A responsive video gallery template with a functional lightbox<br />&ndash;&gt;-->
<!--&lt;!&ndash;						designed by Templated and released under the Creative Commons License.</p>&ndash;&gt;-->
<!--					<div class="container">&lt;!&ndash; 搜索框 &ndash;&gt;-->
<!--						<div class="search bar3">-->
<!--							<form action="" method="post">-->
<!--								<label>-->
<!--									<input type="text" placeholder="搜索我的收藏...">-->
<!--								</label>-->
<!--								<button type="submit" @click="search_user($event)"></button>-->
<!--							</form>-->
<!--						</div>-->
<!--					</div>-->
<!--				</header>-->
<!--			</div>-->
<!--		</section>-->

<!--    <user-uploads></user-uploads>-->
<!--    <test-images></test-images>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--    import merge from 'webpack-merge';-->
<!--    import ImageStream1 from './ImagePage/ImageStream(1)'-->
<!--    export default {-->
<!--        name: 'Channel',-->
<!--        components:{-->
<!--            'user-uploads': ImageStream,-->
<!--            'test-images':  ImageStream1-->
<!--        },-->
<!--        data(){-->
<!--            return {-->
<!--                msg:"搜索我的上传为...",-->
<!--                keyw: 'all',-->
<!--            };-->
<!--        },-->
<!--        methods:{-->
<!--          search_user(e){-->
<!--              this.keyw = e.target.text.trim();-->
<!--              this.$route.push({query:merge(this.$route.query,{'key': this.keyw})});-->
<!--          },-->
<!--        }-->
<!--}-->
<!--</script>-->

<!--<style scoped>-->
<!--.favorite {-->
<!--    padding-top: 4.25em;-->
<!--    min-height: 60vh;-->
<!--}-->
<!--#banner {-->
<!--    padding: 0;-->
<!--    /*background-image: url("../assets/images/Veil.jpg");*/-->
<!--}-->
<!--#banner h1 {-->
<!--    font-size: 3em;-->
<!--    font-weight: 400;-->
<!--    font-family: "sans-serif";-->
<!--    margin: 0;-->
<!--}-->
<!--#banner .avatar img {-->
<!--    width: 9em;-->
<!--}-->
<!--div.search {-->
<!--    padding-top: 1.5em;-->
<!--}-->
<!--/* Search */-->
<!--.container {-->
<!--		bottom: 0;-->
<!--		height: 107px;-->
<!--		position: absolute;-->
<!--		line-height: 150px;-->
<!--		right: 120px;-->
<!--		width: 500px;-->
<!--		margin: 0 auto;-->
<!--	}-->

<!--	button.container {-->
<!--		-webkit-appearance: button;-->
<!--		-webkit-writing-mode: horizontal-tb !important;-->
<!--		text-rendering: auto;-->
<!--		color: buttontext;-->
<!--		letter-spacing: normal;-->
<!--		word-spacing: normal;-->
<!--		text-transform: none;-->
<!--		text-indent: 0;-->
<!--		text-shadow: none;-->
<!--		display: inline-block;-->
<!--		text-align: center;-->
<!--		align-items: flex-start;-->
<!--		cursor: default;-->
<!--		background-color: buttonface;-->
<!--		box-sizing: border-box;-->
<!--		margin: 0;-->
<!--		font: 400 13.3333px Arial;-->
<!--		padding: 1px 6px;-->
<!--		border-width: 2px;-->
<!--		border-style: outset;-->
<!--		border-color: buttonface;-->
<!--		border-image: initial;-->
<!--	}-->
<!--	/*div.search {padding: 0 0;}*/-->

<!--	body.container {-->
<!--		margin: 0;-->
<!--		padding: 0;-->
<!--		background: #494A5F;-->
<!--		font-weight: 500;-->
<!--		font-family: "Microsoft YaHei", "宋体", "Segoe UI", "Lucida Grande", Helvetica, Arial, sans-serif, FreeSans, Arimo;-->
<!--	}-->
<!--		form {-->
<!--            position: relative;-->
<!--            margin: 0 0 -6.2em 0 ;-->
<!--        }-->

<!--        input, button {-->
<!--            border: none;-->
<!--            outline: none;-->
<!--        }-->

<!--        input {-->
<!--            width: 100%;-->
<!--            height: 33px;-->
<!--            padding-left: 13px;-->
<!--        }-->

<!--        button {-->
<!--            /*height: 42px;*/-->
<!--            /*width: 42px;*/-->
<!--            cursor: pointer;-->
<!--            position: absolute;-->
<!--        }-->

<!--	::-webkit-input-placeholder { /* WebKit, Blink, Edge */-->
<!--		color: rgba(198, 196, 196, 0.73);-->
<!--	}-->

<!--		.bar1 form {-->
<!--			width: 200px;-->
<!--			margin: 0 0 0 12em ;-->
<!--		}-->
<!--        .bar1 input {-->
<!--			border: 0;-->
<!--			padding: 5px 40px 5px 13px;-->
<!--			font-size: 14px;-->
<!--			border-bottom: solid 1px;-->
<!--            text-shadow: none;-->
<!--			border-radius: 6px;-->
<!--            background: #ffffff;-->
<!--            color: #343232;-->
<!--			outline: none;-->
<!--        }-->
<!--        .bar1 button {-->
<!--            top: 59px;-->
<!--            right: 0;-->
<!--            background: rgb(238, 106, 132);-->
<!--            border-radius: 0 5px 5px 0;-->
<!--			height: 33px;-->
<!--			width: 35px;-->
<!--			cursor: pointer;-->
<!--			position: absolute;-->
<!--			border: none;-->
<!--        }-->
<!--        .bar1 button:before {-->
<!--            content: "\f002";-->
<!--			font-family: FontAwesome, serif;-->
<!--            font-size: 16px;-->
<!--            color: #ffffff;-->
<!--        }-->

<!--		.bar3 form {-->
<!--			width: 400px;-->
<!--			margin: 3em 0 0 3.5em ;-->
<!--		}-->
<!--        .bar3 input {-->
<!--			border: 0;-->
<!--			padding: 5px 40px 5px 13px;-->
<!--			font-size: 14px;-->
<!--			border-bottom: solid 1px;-->
<!--            text-shadow: none;-->
<!--			border-radius: 6px;-->
<!--            background: #ffffff;-->
<!--            color: #343232;-->
<!--			outline: none;-->
<!--		}-->
<!--        .bar3 button {-->
<!--             top: 59px;-->
<!--            right: 0;-->
<!--            border-radius: 0 5px 5px 0;-->
<!--			height: 32px;-->
<!--			width: 32px;-->
<!--			cursor: pointer;-->
<!--			position: absolute;-->
<!--			border: none;-->
<!--			background: #ffffff;-->
<!--        }-->
<!--        .bar3 button:before {-->
<!--            content: "\f002";-->
<!--			font-family: FontAwesome, serif;-->
<!--            font-size: 16px;-->
<!--            color: rgb(238, 106, 132);-->
<!--        }-->

<!--		@media screen and (max-width: 1280px) {-->
<!--			.bar1 {-->
<!--				padding: 0;-->
<!--				font-size: 14px;-->
<!--			}-->
<!--		}-->

<!--		@media screen and (max-width: 980px) {-->

<!--			.bar1 {-->
<!--				padding: 0;-->
<!--				font-size: 14px;-->
<!--			}-->
<!--			.bar1 form {-->
<!--				width: 180px;-->
<!--				margin: 0 0 0 12em;-->
<!--			}-->
<!--		}-->

<!--		@media screen and (max-width: 736px) {-->

<!--			.bar1 {-->
<!--				padding: 0;-->
<!--				font-size: 14px;-->
<!--			}-->
<!--			.bar1 form {-->
<!--				width: 150px;-->
<!--				margin: 0 0 0 18em;-->
<!--			}-->
<!--			.bar1 input{-->
<!--				height: 80%;-->
<!--				width: 80%	;-->
<!--				padding: 5px 30px 5px 10px;-->
<!--				font-size: 8px;-->
<!--			}-->
<!--			.bar1 button {-->
<!--				top: 4em;-->
<!--				margin-top: 7px;-->
<!--				height: 15%;-->
<!--				width: 15%;-->
<!--			}-->
<!--		}-->
<!--</style>-->
