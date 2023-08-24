<template>
  <div>
    <div class="ui main container">

      <img class="ui centered medium image" src="../assets/Bulkbuddy_rogo.png" alt="Bulkbuddy_rogo">

      <!-- ローディング表示 -->
      <div class="ui active inverted page dimmer" v-if="isCallingApi">
        <div class="ui text loader">Loading</div>
      </div>

      <div class="ui segment">
        <!-- エラーメッセージ-->
        <p class="ui negative message" v-if="errorMsg">
          <i class="close icon" @click="clearError"></i>
          <span class="header">エラーが発生しました！</span>
          {{ errorMsg }}
        </p>

        <!-- submitイベントを拾って、preventにて規定のアクションを中止し、submitメソッドを呼び出す。-->
        <form class="ui large form" @submit.prevent="submit">
          <h3 class="ui centered header title-text">
            {{ toggledTitleText }} <br> {{ toggledSubTitleText }}
          </h3>
          
          <div class="field">
            <p>ユーザー名</p>
            <input v-model="user.userId" type="text" placeholder="ユーザー名を入力" />
          </div>

          
          <div class="field">
            <p>パスワード</p>
            <input v-model="user.password" type="password" placeholder="パスワードを入力" />
          </div>

          <div class="field" v-if="!isLogin">
            <p>ユーザー名</p>
            <i class="tag icon"></i>
            <input v-model="user.nickname" type="text" placeholder="Nickname" />
          </div>

          <div class="field" v-if="!isLogin">
            <div class="ui left icon input">
              <i class="calendar icon"></i>
              <input v-model.number="user.age" type="number" min="0" placeholder="Age" />
            </div>
          </div>

          
          <div class="ui centered grid">
            <div class="center aligned column">
              <button class="ui button orange-button" :disabled="isButtonDisabled" type="submit">{{ submitBtnText }}</button>
            </div>
          </div>
        </form>
      </div>

      <div class="ui centered grid">
        <div class="center aligned column">
          <button @click="toggleMode" class="ui button grey-button" type="submit">{{ toggledBtnText }}</button>
        </div>
      </div>
  
    </div>
  </div>
</template>

<script>
  // 必要なものはここでインポートする
  // @は/srcの同じ意味です
  // import something from '@/components/something.vue';
  import { baseUrl } from '@/assets/config.js';

  export default {
    name: 'Login',

    components: {
      // 読み込んだコンポーネント名をここに記述する
    },

    data() {
      // Vue.jsで使う変数はここに記述する
      return {
        isLogin: true,
        user: {
          userId: null,
          password: null,
          nickname: null,
          age: null
        },
        errorMsg: '', // 発展課題のエラーメッセージ用
        isCallingApi: false // 発展課題のローディング表示用
      };
    },

    computed: {
      // 計算した結果を変数として利用したいときはここに記述する

      // 発展課題のボタン活性/非活性用
      isButtonDisabled() {
        const { userId, password, nickname, age } = this.user;
        return this.isLogin ?
          !userId || !password :
          !userId || !password || !nickname || !age;
      },
      
      toggledTitleText() {
        return this.isLogin ? 'ログイン' : '目標設定には新規登録が必要です'
      },
      
      toggledSubTitleText() {
        return this.isLogin ? '' : 'あなたについて教えてください'
      },
      
      submitBtnText() {
        return this.isLogin ? 'ログイン' : '新規登録'
      },

      toggledBtnText() {
        return this.isLogin ? '新規登録はこちら' : 'ログインはこちら'
      }
    },


    methods: {
      // Vue.jsで使う関数はここで記述する

      // 発展課題のエラーメッセージ用
      clearError() {
        this.errorMsg = ''
      },

      toggleMode() {
        this.isLogin = !this.isLogin;
      },

      async submit() {
        if (this.isCallingApi) {
          return;
        }
        this.isCallingApi = true;

        const path = this.isLogin ? '/user/login' : '/user/signup';
        const { userId, password, nickname, age } = this.user;
        const reqBody = this.isLogin ? { userId, password } : { userId, password, nickname, age };

        try {
          /* global fetch */
          const res = await fetch(baseUrl + path, {
            method: 'POST',
            body: JSON.stringify(reqBody)
          });

          const text = await res.text();
          const jsonData = text ? JSON.parse(text) : {}

          // fetchではネットワークエラー以外のエラーはthrowされないため、明示的にthrowする
          if (!res.ok) {
            const errorMessage = jsonData.message ?? 'エラーメッセージがありません';
            throw new Error(errorMessage);
          }

          window.localStorage.setItem('token', jsonData.token);
          window.localStorage.setItem('userId', this.user.userId);

          this.$router.push({ name: 'Home' });
        }
        catch (e) {
          console.error(e);
          this.errorMsg = e;
        }
        finally {
          this.isCallingApi = false;
        }
      }
    },
  }
</script>

<style scoped>
  /* このコンポーネントだけに適用するCSSはここに記述する */
.orange-button {
  background-color: #F68712;
  color: white;
  width: 25%;
  margin: 20px;
}
.grey-button {
  background-color: #333;
  color: white;
  width: 24%;
  margin: 20px;
}
.title-text {
  padding: 20px;
}
</style>
